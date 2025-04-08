import socket 
import argparse 
from  classforCLI import Request, Responses
from log import setup_logger
import logging
import toml

setup_logger()
logger=logging.getLogger('MyProgramm')
logger.info('programm is ready')


parser = argparse.ArgumentParser(
    prog="SMS sender CLI", 
    description="Программа для отправки сообщений", 
    usage='%(prog)s sender recipient message'
)
parser.add_argument('sender', type=str, help='Номер отправителя')
parser.add_argument('recipient', type=str, help='Номер получателя')
parser.add_argument('message', type=str, help='Текст сообщения')

#вывод справки  если аргументы не переданы
import sys
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
#формирование словаря из полученных данных от пользователя
body: dict[str, str] = vars(args)
logger.info(f'Получены параметры: {body}')
for_classCLI = Request(body)
logger.info(f'Создан объект запроса с параметрами: {body}')

with open("config.toml") as f:
    data = toml.load(f)
url = data['URL']
host_url = url.split('/')[2].split(':')[0]
port_url = int(''.join(url.split('/')[2].split(':')[1]))

try:
    #создание сокета
    sock = socket.socket() 
    sock.settimeout(10)  # 10 секунд таймаут
    #подключение к порту
    sock.connect((host_url, port_url))
    logger.info(f'Подключение к порту {host_url, port_url}')
    #отправка запроса в байтах 
    send_message = for_classCLI.to_bytes()
    logger.info(f'HTTP {send_message.decode()}')
    sock.send(send_message)
    logger.info(f'Отправка запроса в байтах {send_message}')
    #возвращаемый ответ 
    reply = sock.recv(4096)

    #декодируем ответ и отправляем в вывод  
    decode_bytes = Responses()
    decode_bytes.from_bytes(reply)
    answer_from_server = decode_bytes.from_bytes(reply)
    logger.info(f'Декодируемый вывод {answer_from_server}')

    print(answer_from_server)
except socket.timeout:
    logger.error('Превышено время ожидания ответа от сервера')
    print('Ошибка: Превышено время ожидания ответа от сервера')
except Exception as e:
    logger.error(f'Непредвиденная ошибка: {e}')
    print(f'Ошибка: {e}')
except ConnectionError as e:
    logger.error(f'Ошибка подключения: {e}')
    print(f'Ошибка: Не удалось подключиться к серверу. {e}')
except socket.gaierror:
    logger.error(f'Ошибка разрешения имени хоста: {host_url}')
    print(f'Ошибка: Не удалось разрешить имя хоста {host_url}')
finally:
    try:
        sock.close()
        logger.info('Соединение закрыто')
    except:
        pass



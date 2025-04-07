import socket 
import argparse 
from  classforCLI import Request, Responses
from log import setup_logger
import logging

setup_logger()
logger=logging.getLogger('MyProgramm')
logger.info('programm is ready')
parser = argparse.ArgumentParser(prog="Programm for message", usage='%(prog)s')
parser.add_argument('sender', type=str, help='print number for request')
parser.add_argument('recipient', type=str, help='print number for responses')
parser.add_argument('message', type=str, help='print message')
parser.print_help()

args = parser.parse_args()
#формирование словаря из полученных данных от пользователя
body = vars(args)

for_classCLI = Request(body)
logger.info(f'send text for HTTPRequest {body}')


sock = socket.socket() 
sock.connect(('localhost', 4010))

send_message = for_classCLI.to_bytes()
print(send_message.decode())
sock.send(send_message)

logger.info(f'send HTTPRequest {send_message}')
reply = sock.recv(4096)


decode_bytes = Responses()
decode_bytes.from_bytes(reply)

answer_from_server = decode_bytes.from_bytes(reply)
logger.info(f'received response {answer_from_server}')

print(answer_from_server)


# CLI для отправки SMS-сообщений

## Описание
Программа предназначена для отправки SMS-сообщений через HTTP-запросы. Она использует сокеты для взаимодействия с сервером и поддерживает конфигурацию через файл `config.toml`.

## Установка
1. Убедитесь, что у вас установлен Python 3.8 или выше.
2. Создайте виртуальное окружение:
```bash
   python -m venv venvCLI
   source venvCLI/bin/activate     # Для Linux/MacOS
   venvCLI\Scripts\activate        # Для Windows
```

## Конфигурация
Создайте файл `config.toml` в корневой директории проекта со следующим содержимым:
```toml
URL='http://localhost:4010/send_sms'
user='ВашеИмяПользователя'
password='ВашПароль'
```
    (Для работы с типом файла TOML не забудье проверить наличие библиотеки toml)

## Запуск
Для запуска программы используйте следующую команду:
```bash(в командной строке)
python SWOYOprogramm.py <sender> <recipient> <message>
Где:
- `<sender>` — номер отправителя.
- `<recipient>` — номер получателя.
- `<message>` — текст сообщения.

Пример:
```bash
python SWOYOprogramm.py +4123 +123 "HELLO"
```

## Тестирование
Для тестирования программы можно использовать мок-сервер:
1. Скачайте Prism: [Prism Releases](https://github.com/stoplightio/prism/releases).
2. Запустите мок-сервер:
   ```bash
   ./prism-cli-macos mock sms-platform.yaml
   ```
3. Программа будет взаимодействовать с сервером по адресу `http://localhost:4010/send_sms`.

Для запуска тестов используйте:
```bash
pytest test_SWOYOprogramm.py test_forprogramm.py
```

## Логирование
Логи программы сохраняются в файл `app.log` и содержат информацию о переданных параметрах и ответах сервера.
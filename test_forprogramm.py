from classforCLI import Responses, Request
decode_bytes = Responses()

def test_tobytes(): 
    name = 'qwe'
    password = 123
    basicAuth = [name, password]
    url = "http://anysite:1122/send_sms"
    host = url.split('/')[2].split(':')[0]
    path = f'/{url.split('/')[3]}'

    sender, recipient, message = "+12323", "+655346", "HELLO"
    json_body = {
        'sender': sender,
        'recipient': recipient,
        'message': message
    }

    http_request = (
        f"POST {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Authorization: Basic {basicAuth}\r\n"
        f"Content-Type: application/json\r\n"
        f"Content-Length: {len(json_body)}\r\n"
        f"\r\n"
        f"{json_body}"
    )
    
    assert http_request == "POST /send_sms HTTP/1.1\r\nHost: anysite\r\nAuthorization: Basic ['qwe', 123]\r\nContent-Type: application/json\r\nContent-Length: 3\r\n\r\n{'sender': '+12323', 'recipient': '+655346', 'message': 'HELLO'}"

# def test_tobytes():
#     json_body = {'sender': 'num1', 'recipient': 'num2', 'message': 'text'}
#     basicAuth = ['Gera', '123']
#     url = 'localhost:4010/send_sms'
#     host = url.split('/')[0]
#     path = "/send_sms"
#     http_request = (
#             f"POST {path} HTTP/1.1\r\n"
#             f"Host: {host}\r\n"
#             f"Authorization: Basic {basicAuth}\r\n"
#             f"Content-Type: application/json\r\n"
#             f"Content-Length: {len(json_body)}\r\n"
#             f"\r\n"
#             f"{json_body}"
#         )
#     assert http_request == "POST /send_sms HTTP/1.1\r\nHost: localhost:4010\r\nAuthorization: Basic ['gera', '123']\r\nContent-Type: application/json\r\nContent-Length: 3\r\n\r\n{'sender': 'num1', 'recipient': 'num2', 'message': 'text'}"
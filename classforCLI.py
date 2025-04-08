import json
from base64 import b64encode
import toml

class Request:
    def __init__(self, body: dict):
        self.sender = body['sender']
        self.recipient = body['recipient']
        self.message = body['message']

        with open("config.toml") as f:  
            data = toml.load(f)
        self.url = data['URL']
        self.password = data['password']
        self.name = data['user']

    def to_bytes(self) -> bytes:
        auth_str = f'{self.name}:{self.password}'
        basicAuth = b64encode(auth_str.encode()).decode()

        host = self.url.split('/')[2].split(':')[0]
        path = f'/{self.url.split('/')[3]}'
        if not path:
            path = "/send_sms"
        json_body = json.dumps({
            'sender': self.sender,
            'recipient': self.recipient,
            'message': self.message
        })

        http_request = (
            f"POST {path} HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"Authorization: Basic {basicAuth}\r\n"
            f"Content-Type: application/json\r\n"
            f"Content-Length: {len(json_body)}\r\n"
            f"\r\n"
            f"{json_body}"
        )
        
        return http_request.encode()
    
class Responses:
    def from_bytes(self, reply: bytes) -> str:
        decode_reply = reply.decode().split('\r\n')
        code = decode_reply[0]
        body = decode_reply[-1] 
        body = body.replace('{', '')
        body = body.replace('}', '')
        body = body.replace('"', '')
        body = body.replace(',', ", ")
        
        return f'Status code = {' '.join(code.split(' ')[1:])}\nBody = {body}'
        

        


import json
from base64 import b64encode
import toml

class Request:
    with open("config.toml") as f:
        data = toml.load(f)
    def __init__(self, body: list):
        self.sender = body['sender']
        self.recipient = body['recipient']
        self.message = body['message']
        self.url = self.data['URL']
        self.password = self.data['password']
        self.name = self.data['user']

    def to_bytes(self) -> bytes:
        auth_str = f'self.password:self.name'
        basicAuth = b64encode(auth_str.encode()).decode()

        host = self.url.split()[0]
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
        print(http_request)
        return http_request.encode()
    
class Responses:
    def from_bytes(self, reply: bytes) -> str:
        text_reply = list(reply) 
        resp_code = []
        body_text = []
        for i in text_reply[9:12]:
            resp_code.append(i)

        start = text_reply.index(123)
        for i in text_reply[start:]:
            body_text.append(i)

        return f'code: {bytes(resp_code).decode()}, body: {bytes(body_text).decode()}'
        # text = back.decode().split('\r\n')
        # resp_code = text[0]
        # body_text = text[-1]
        # return f'code: {resp_code}, body: {body_text}'
        
            

        


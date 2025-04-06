import json
from base64 import b64encode
import toml

class Request:
    with open("config.toml") as f:
        data = toml.load(f)
    def __init__(self, body):
        self.sender = body['sender']
        self.recipient = body['recipient']
        self.message = body['message']
        self.url = self.data['URL']
        self.password = self.data['password']
        self.name = self.data['user']

    def to_bytes(self):
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

        return http_request.encode()
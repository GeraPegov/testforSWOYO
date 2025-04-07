from classforCLI import Responses, Request
decode_bytes = Responses()
test_data = [72, 84, 84, 80, 47, 49, 46, 49, 32, 50, 48, 48, 32, 79, 75, 13, 10, 65, 99, 99, 101, 115, 115, 45, 67, 111, 110, 116, 114, 111, 108, 45, 65, 108, 108, 111, 119, 45, 79, 114, 105, 103, 105, 110, 58, 32, 42, 13, 10, 65, 99, 99, 101, 115, 115, 45, 67, 111, 110, 116, 114, 111, 108, 45, 65, 108, 108, 111, 119, 45, 72, 101, 97, 100, 101, 114, 115, 58, 32, 42, 13, 10, 65, 99, 99, 101, 115, 115, 45, 67, 111, 110, 116, 114, 111, 108, 45, 65, 108, 108, 111, 119, 45, 67, 114, 101, 100, 101, 110, 116, 105, 97, 108, 115, 58, 32, 116, 114, 117, 101, 13, 10, 65, 99, 99, 101, 115, 115, 45, 67, 111, 110, 116, 114, 111, 108, 45, 69, 120, 112, 111, 115, 101, 45, 72, 101, 97, 100, 101, 114, 115, 58, 32, 42, 13, 10, 67, 111, 110, 116, 101, 110, 116, 45, 116, 121, 112, 101, 58, 32, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 47, 106, 115, 111, 110, 13, 10, 67, 111, 110, 116, 101, 110, 116, 45, 76, 101, 110, 103, 116, 104, 58, 32, 52, 50, 13, 10, 68, 97, 116, 101, 58, 32, 77, 111, 110, 44, 32, 48, 55, 32, 65, 112, 114, 32, 50, 48, 50, 53, 32, 48, 55, 58, 51, 49, 58, 53, 48, 32, 71, 77, 84, 13, 10, 67, 111, 110, 110, 101, 99, 116, 105, 111, 110, 58, 32, 107, 101, 101, 112, 45, 97, 108, 105, 118, 101, 13, 10, 75, 101, 101, 112, 45, 65, 108, 105, 118, 101, 58, 32, 116, 105, 109, 101, 111, 117, 116, 61, 53, 13, 10, 13, 10, 123, 34, 115, 116, 97, 116, 117, 115, 34, 58, 34, 115, 117, 99, 99, 101, 115, 115, 34, 44, 34, 109, 101, 115, 115, 97, 103, 101, 95, 105, 100, 34, 58, 34, 49, 50, 51, 52, 53, 54, 34, 125]
def test_frombytes():
    text_reply = test_data
    resp_code = []
    body_text = []
    for i in text_reply[9:12]:
        resp_code.append(i)

    start = text_reply.index(123)
    for i in text_reply[start:]:
        body_text.append(i)

    assert bytes(resp_code).decode() == '200'
    assert bytes(body_text).decode() == '{"status":"success","message_id":"123456"}'

def test_tobytes():
    json_body = {'sender': 'num1', 'recipient': 'num2', 'message': 'text'}
    basicAuth = ['gera', '123']
    url = 'localhost:4010/send_sms'
    host = url.split('/')[0]
    path = "/send_sms"
    http_request = (
            f"POST {path} HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"Authorization: Basic {basicAuth}\r\n"
            f"Content-Type: application/json\r\n"
            f"Content-Length: {len(json_body)}\r\n"
            f"\r\n"
            f"{json_body}"
        )
    assert http_request == """POST /send_sms HTTP/1.1\r\nHost: localhost:4010\r\nAuthorization: Basic ['gera', '123']\r\nContent-Type: application/json\r\nContent-Length: 3\r\n\r\n{'sender': 'num1', 'recipient': 'num2', 'message': 'text'}"""
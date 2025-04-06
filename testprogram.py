import socket 
import argparse 
from  classforCLI import Request

parser = argparse.ArgumentParser(prog="Programm for message", usage='%(prog)s')

parser.add_argument('sender', type=str, help='print number for request')
parser.add_argument('recipient', type=str, help='print number for responses')
parser.add_argument('message', type=str, help='print message')
parser.print_help()

args = parser.parse_args()

body = vars(args)
for_classCLI = Request(body)


sock = socket.socket() 
sock.connect(('localhost', 4010))
send_message = for_classCLI.to_bytes()
sock.send(send_message)

back = sock.recv(4096)
print(back.decode())
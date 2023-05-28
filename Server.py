from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging

# Задавам конфигурация на FTP сървъра

ftp_address = '127.0.0.1'
ftp_port = '2121'

# Потребители

users = [{'directory': './ftp/user1', 'username': 'user1', 'password': 'password1'},
         {'directory': './ftp/user2', 'username': 'user2', 'password': 'password2'},
         {'directory': './ftp/user3', 'username': 'user3', 'password': 'password3'},
         ]

# Регистрирам потребителите
authorizer = DummyAuthorizer()
for user in users:
    authorizer.add_user(user['username'], user['password'], user['directory'], perm='elradfmwMT')

# Define the FTP handler
handler = FTPHandler
handler.authorizer = authorizer

# Start the FTP server
server = FTPServer((ftp_address, ftp_port), handler)

# logging.basicConfig(filename='./log/pyftpd.log', level=logging.INFO)
server.serve_forever()

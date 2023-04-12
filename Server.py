from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define the FTP server settings
ftp_port = 2121
ftp_username = 'username'
ftp_password = 'password'
ftp_directory = '/12b/ftp'

# Define the user authorizer
authorizer = DummyAuthorizer()
authorizer.add_user(ftp_username, ftp_password, ftp_directory, perm='elradfmwMT')

# Define the FTP handler лк;ксфгксдфс
handler = FTPHandler
handler.authorizer = authorizer

# Start the FTP server
server = FTPServer(('192.168.99.104', ftp_port), handler)
server.serve_forever()

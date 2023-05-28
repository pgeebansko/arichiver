from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define the FTP server settings
ftp_port = 9999
ftp_username = 'USER3'
ftp_password = '2121'
ftp_directory = '/DZI2023/archiver/ftp'

# Define the user authorizer
authorizer = DummyAuthorizer()
authorizer.add_user(ftp_username, ftp_password, ftp_directory, perm='elradfmwMT')

# Define the FTP handler лк;ксфгксдфс
handler = FTPHandler
handler.authorizer = authorizer

# Start the FTP server
server = FTPServer(('192.168.99.60', ftp_port), handler)
server.serve_forever()

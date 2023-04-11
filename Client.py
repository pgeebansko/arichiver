import ftplib

# set up connection parameters
ftp_server = '192.168.99.103'
ftp_port = 2121
ftp_username = 'USER3'
ftp_password = '2121'

# connect to FTP server
ftp = ftplib.FTP()
ftp.connect(ftp_server, ftp_port)
ftp.login(ftp_username, ftp_password)

# list files on server
print('Files on server:')
files = ftp.dir()
print(files)

with open('test.txt', 'w') as f:
    f.write('This is a test file.')

# upload file to server
filename = 'test.txt'
with open(filename, 'rb') as f:
    ftp.storbinary(f'STOR {filename}', f)

# download file from server
filename = 'test.txt'
with open(filename, 'wb') as f:
    ftp.retrbinary(f'RETR {filename}', f.write)



# close connection
ftp.quit()

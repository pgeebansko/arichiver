import ftplib
import Client_settings
import glob
import time


# четене на конфигурационните параметри
settings = Client_settings.Settings()

while True:
    dir_path = settings.working_dir + settings.file_type
    res = glob.glob(dir_path, recursive=True)
    print(res)

    # свързване с FTP сървъра
    ftp = ftplib.FTP()

    for path in res:
        # обхождам файл по файл целия списък на файлове от папката
        ftp.connect(settings.ftp_server, settings.ftp_port)
        ftp.login(settings.ftp_username, settings.ftp_password)

        # upload file to server
        filename = 'test.txt'
        with open(filename, 'rb') as f:
            ftp.storbinary(f'STOR {filename}', f)

    # close connection
    ftp.quit()
    time.sleep(10)

from configparser import ConfigParser

INI_FILE_NAME = 'client.ini'


class Settings:
    ftp_server = '192.168.99.103'
    ftp_port = 2121
    ftp_username = 'USER3'
    ftp_password = '2121'
    working_dir = ''
    file_type = ''

    def __init__(self):
        self.config = ConfigParser()
        self.read_settings()

    def read_settings(self):
        self.config.read(INI_FILE_NAME)

        self.ftp_server = self.config.get('SERVER', 'IP_address')
        self.ftp_port = int(self.config.get('SERVER', 'port'))
        self.ftp_username = self.config.get('USER', 'name')
        self.ftp_password = self.config.get('USER', 'password')
        self.file_type = self.config.get('FILES', 'type')
        self.working_dir = self.config.get('FILES', 'dir')

    def write_settings(self):
        self.config.set('SERVER', 'IP_address', self.ftp_server)
        self.config.set('SERVER', 'port', self.ftp_port)
        self.config.set('USER', 'name', self.ftp_username)
        self.config.set('USER', 'password', self.ftp_password)
        self.config.set('FILES', 'type', self.file_type)
        self.config.set('FILES', 'dir', self.working_dir)

        with open(INI_FILE_NAME, 'w') as configfile:    # save
            self.config.write(configfile)









class FTPClientSettings:
    dir = r'C:\ggb\GEORGI\DZI_22_23'
    files = r'\*.*'

    def get_dir(self):
        return self.dir

    def get_files(self):
        return self.dir+self.files

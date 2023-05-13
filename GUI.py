from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QTextEdit, QInputDialog
from PyQt5.QtGui import QIcon
import sys


class FtpClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.delete_button = None
        self.status_text = None
        self.download_button = None
        self.upload_button = None
        self.disconnect_button = None
        self.connect_button = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("FTP Client")
        self.setGeometry(100, 100, 500, 300)

        # Create the buttons
        self.connect_button = QPushButton("Connect", self)
        self.connect_button.move(10, 10)
        self.connect_button.clicked.connect(self.connect_ftp)
        
        self.disconnect_button = QPushButton("Disconnect", self)
        self.disconnect_button.move(110, 10)
        self.disconnect_button.setEnabled(False)
        self.disconnect_button.clicked.connect(self.disconnect_ftp)

        self.upload_button = QPushButton("Upload", self)
        self.upload_button.move(210, 10)
        self.upload_button.setEnabled(False)
        self.upload_button.clicked.connect(self.upload_file)

        self.download_button = QPushButton("Download", self)
        self.download_button.move(310, 10)
        self.download_button.setEnabled(False)
        self.download_button.clicked.connect(self.download_file)

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.move(410, 10)
        self.delete_button.setEnabled(False)
        self.delete_button.clicked.connect(self.delete_file)

        # Create the status text box
        self.status_text = QTextEdit(self)
        self.status_text.setGeometry(10, 50, 480, 240)
        self.status_text.setReadOnly(True)

        # Show the window
        self.show()

    def connect_ftp(self):
        # Prompt the user for the FTP server details
        host, ok = QInputDialog.getText(self, "Connect to FTP Server", "Enter host name:")
        if ok:
            port, ok = QInputDialog.getInt(self, "Connect to FTP Server", "Enter port number:", 2121)
            if ok:
                user, ok = QInputDialog.getText(self, "Connect to FTP Server", "Enter user name:")
                if ok:
                    password, ok = QInputDialog.getText(self, "Connect to FTP Server", "Enter password:")
                    if ok:
                        self.status_text.append(f"Connected to FTP server {host}:{port}")
                        self.connect_button.setEnabled(False)
                        self.disconnect_button.setEnabled(True)
                        self.upload_button.setEnabled(True)
                        self.download_button.setEnabled(True)
                        self.delete_button.setEnabled(True)

    def disconnect_ftp(self):
        # Disconnect from the FTP server
        self.status_text.append("Disconnected from FTP server")
        self.connect_button.setEnabled(True)
        self.disconnect_button.setEnabled(False)
        self.upload_button.setEnabled(False)
        self.download_button.setEnabled(False)

    def upload_file(self):
        # Prompt the user to select a file to upload
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Upload")
        if file_path:
            # Get the filename and upload the file to the FTP server
            filename = file_path.split("/")[-1]
            self.status_text.append(f"File {filename} uploaded successfully")

    def download_file(self):
        # Prompt the user to select a remote file to download
        remote_path, _ = QFileDialog.getOpenFileName(self, "Select File to Download", filter="All Files (*)")
        if remote_path:
            # Get the filename and download the file from the FTP server
            filename = remote_path.split("/")[-1]
            self.status_text.append(f"File {filename} downloaded successfully")

    def delete_file(self):
        # Prompt the user to select a remote file to delete
        remote_path, _ = QFileDialog.getOpenFileName(self, "Select File to Delete")
        if remote_path:
            # Get the filename and prompt the user to confirm deletion
            filename = remote_path.split("/")[-1]
            confirm_delete, _ = QInputDialog.getMultiLineText(self, "Delete File",
                                                              f"Are you sure you want to delete {filename}?")

            if confirm_delete.strip().lower() == "yes":
                # Delete the file from the FTP server
                self.status_text.append(f"File {filename} deleted successfully")
            else:
                self.status_text.append("File deletion cancelled")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ftp_client = FtpClient()
    sys.exit(app.exec_())


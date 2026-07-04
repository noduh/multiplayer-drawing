from ui.connection import Ui_Connection
from PySide6 import QtCore, QtWidgets


class ConnectionWindow(QtWidgets.QWidget, Ui_Connection):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connect_button.clicked.connect(self.connect_button_handler)

    @QtCore.Slot()
    def connect_button_handler(self):
        ip = self.ip_input.text()
        port = self.port_input.text()

        print(f"IP: {ip}\nPort: {port}")
        self.close()

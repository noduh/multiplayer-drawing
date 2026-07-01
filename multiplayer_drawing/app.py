import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel(
            "Hello World", alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )

        self.layout_main = QtWidgets.QVBoxLayout(self)
        self.layout_main.addWidget(self.text)
        self.layout_main.addWidget(self.button)

        self.button.clicked.connect(self.magic)
    
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

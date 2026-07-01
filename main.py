from multiplayer_drawing import MyWidget
from PySide6 import QtWidgets, QtUiTools
import sys


def main():
    app = QtWidgets.QApplication([])

    window = QtUiTools.QUiLoader().load("ui/connection.ui")
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

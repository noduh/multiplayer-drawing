from multiplayer_drawing import ConnectionWindow
from PySide6 import QtWidgets, QtUiTools
import sys


def main():
    app = QtWidgets.QApplication([])
    window = ConnectionWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

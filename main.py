import sys
from PyQt5 import QtWidgets, QtCore
from Application import *


def main():
    app = QtWidgets.QApplication([])
    application = Application()
    application.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    application.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

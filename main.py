# coding=utf-8

"""
__Author__ = "Amosz"
"""


import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow
from admin_window import AdminWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # man_win = MainWindow()
    # man_win.show()

    main_win = AdminWindow()
    main_win.show()

    sys.exit(app.exec_())

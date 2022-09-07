# coding=utf-8

"""
__Author__ = "Amosz"
"""

import sys
from PyQt5.QtWidgets import QApplication

from main_win import AudioPlayer

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = AudioPlayer()
    win.show()

    sys.exit(app.exec_())

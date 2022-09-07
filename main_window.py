# coding=utf-8

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QPushButton, QInputDialog, QMessageBox

import json


class MainWindow(QMainWindow):
    # 程序的主界面
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        with open("./conf.json", 'r', encoding="utf-8") as f:
            self.conf_data = json.load(f)

        self.setWindowTitle(self.conf_data.get("title", "密室逃脱"))

        # 设置背景图片
        self.setStyleSheet(f"background-color: {self.conf_data['background_color']};")
        # palette = QPalette()
        # palette.setBrush(self.backgroundRole(), QBrush(QPixmap('./images/1.jpeg')))
        # self.setPalette(palette)
        # self.setAutoFillBackground(True)

        self.setFixedSize(self.conf_data["main_win"]['window']['width'], self.conf_data["main_win"]['window']['height'])

        # 程序居中
        self.center()

        # 开始测试的按钮
        self.start_button = QPushButton("开始测试", self)
        self.start_button.setFixedSize(self.conf_data["start_button"]["width"], self.conf_data["start_button"]["height"])
        self.start_button.move(self.conf_data["start_button"]["left"], self.conf_data["start_button"]["top"])
        self.start_button.setStyleSheet(self.conf_data["start_button"]["style_sheet"])
        self.start_button.clicked.connect(self.start_test_click)

        # 修改数据的按钮
        self.modify_button = QPushButton("Administration", self)
        self.modify_button.setStyleSheet(self.conf_data["modify_button"]["style_sheet"])
        self.modify_button.setFixedSize(self.conf_data["modify_button"]["width"], self.conf_data["modify_button"]["height"])
        self.modify_button.move(self.conf_data["modify_button"]["left"], self.conf_data["modify_button"]["top"])
        self.modify_button.clicked.connect(self.chmod_data_click)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        self.move(new_left, new_top)

    def start_test_click(self):
        text, ok = QInputDialog.getText(self, '密码验证',
                                        'Enter your password:')

        if ok:
            if text == self.conf_data["start_button"]["password"]:
                pass
            else:
                QMessageBox.critical(self, "警告", "输入密码错误", QMessageBox.Yes)

    def chmod_data_click(self):
        text, ok = QInputDialog.getText(self, '密码验证',
                                        'Enter your password:')

        if ok:
            if text == self.conf_data["modify_button"]["password"]:
                pass
            else:
                QMessageBox.critical(self, "警告", "输入密码错误", QMessageBox.Yes)

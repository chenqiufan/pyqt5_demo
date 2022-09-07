# coding=utf-8

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QTableWidget, QHeaderView, QFrame, QTableWidgetItem, QPushButton, \
    QColorDialog
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt

import json


class AdminWindow(QWidget):

    def __init__(self):
        super(AdminWindow, self).__init__()

        with open("./conf.json", "r", encoding="utf-8") as f:
            self.conf_data = json.load(f)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.conf_data.get("title", "密室逃脱"))

        self.setStyleSheet(f"background-color: {self.conf_data['background_color']};")

        self.setFixedSize(self.conf_data["admin_win"]['window']['width'],
                          self.conf_data["admin_win"]['window']['height'])

        self.center()

        self.form_layout()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        self.move(new_left, new_top)

    def form_layout(self):
        # 获取需要修改的数据: list
        with open("./conf.json", "r", encoding="utf-8") as f:
            form_data = json.load(f)

        # 表的样式
        table_widget = QTableWidget(self)
        table_widget.setFixedSize(self.conf_data["admin_win"]["table"]["width"],
                                  self.conf_data["admin_win"]["table"]["height"])
        table_widget.move(50, 20)
        row, col = len(form_data), 3
        table_widget.setRowCount(row)
        table_widget.setColumnCount(col)
        table_widget.setFrameShape(QFrame.NoFrame)

        # 单元格样式设计
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 表头
        font = QFont("微软雅黑", 10)
        font.setBold(True)
        table_widget.horizontalHeader().setFont(font)
        table_widget.horizontalHeader().setStyleSheet('QHeaderView::section{background:#00FF7F}')
        table_widget.setHorizontalHeaderLabels(["名称", "当前值", "修改值"])

        # 主窗口相关的
        color_button = QPushButton("选择颜色")
        color_button.clicked.connect(self.get_background_color)

        self.form_col("背景颜色", self.conf_data["background_color"], 0, table_widget)
        table_widget.setCellWidget(0, 2, color_button)

        # 程序名
        self.form_col("程序名", self.conf_data["title"], 1, table_widget)  

    def form_col(self, name, pre_val, col_num, table_widget):
        name_item = QTableWidgetItem(name)
        name_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.format_table_cell(name_item)
        table_widget.setItem(col_num, 0, name_item)

        pre_val_item = QTableWidgetItem(pre_val)
        pre_val_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.format_table_cell(pre_val_item)
        table_widget.setItem(col_num, 1, pre_val_item)

    def format_table_cell(self, item):
        # 字体居中
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def get_background_color(self):
        color = QColorDialog.getColor()
        self.setStyleSheet(f"background-color: {color.name()};")
        with open("./conf.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            data["background_color"] = color.name()

        with open("./conf.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def set_cell_val(self):
        # todo
        pass

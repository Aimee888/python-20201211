#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : python-20201211 -> change_window.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/1/22 18:25
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal
import ui_form1
import ui_form2


class MainWin(QWidget):
    show_sub_win_signal = pyqtSignal()  # 该信号用于展示主窗体

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = ui_form1.Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.ui.pushButton.clicked.connect(self.go_sub)

    def go_sub(self):
        self.show_sub_win_signal.emit()


class SubWin(QWidget):
    # 自定义信号
    show_main_win_signal = pyqtSignal()  # 该信号用于展示子窗体

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = ui_form2.Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.ui.pushButton.clicked.connect(self.go_main)

    def go_main(self):
        self.show_main_win_signal.emit()


def show_sub():
    subWin.show()
    myWin.hide()


def show_main():
    myWin.show()
    subWin.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWin()
    myWin.show()
    subWin = SubWin()
    myWin.show_sub_win_signal.connect(show_sub)
    subWin.show_main_win_signal.connect(show_main)
    sys.exit(app.exec_())

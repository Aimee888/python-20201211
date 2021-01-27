#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : python-20201211 -> get_value_from_ui.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/1/27 14:49
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_button import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.ui.pushButton.clicked.connect(self.return_pass)
        self.ui.pushButton_2.clicked.connect(self.return_fail)

    def return_pass(self):
        global result
        result = 0
        self.close()

    def return_fail(self):
        global result
        result = 1
        self.close()


if __name__ == '__main__':
    result = 0
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    app.exec_()
    sys.exit(result)

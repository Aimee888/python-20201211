#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : python-20201211 -> game_2048.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/1/8 11:48
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import Qt
from ui_2048 import Ui_Form
import random


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.init_setting()
        self.init_datas()

        self.game_pass = False
        self.game_over = False
        self.up_game_over = False
        self.down_game_over = False
        self.left_game_over = False
        self.right_game_over = False
        self.count = 0

    def init_setting(self):
        # 隐藏行表头
        self.ui.tableWidget.horizontalHeader().hide()
        # 设置行自适应父容器大小
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置列自适应父容器大小
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置不可选中
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        # 取消聚焦
        self.ui.tableWidget.setFocusPolicy(Qt.NoFocus)
        # 设置表格不可编辑
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置label不可见
        self.ui.label.setVisible(False)
        self.ui.label_2.setVisible(False)
        self.ui.pushButton.setVisible(False)

    def init_datas(self):
        self.generate_randnum()
        self.generate_randnum()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_W or event.key() == Qt.Key_Up:
            self.up_excuted()
        if event.key() == Qt.Key_A or event.key() == Qt.Key_Down:
            self.down_excuted()
        if event.key() == Qt.Key_S or event.key() == Qt.Key_Left:
            self.left_excuted()
        if event.key() == Qt.Key_D or event.key() == Qt.Key_Right:
            self.right_excuted()

    def getcolumn_data(self, num_column):
        column_l = num_column - 1
        column_data = []
        for row_l in range(4):  # 每一行
            cell_str = self.ui.tableWidget.item(row_l, column_l).text()
            column_data.append(int(cell_str))
        # print(column_data)
        return column_data

    def getrow_data(self, num_row):
        row_l = num_row - 1
        row_data = []
        for column_l in range(4):  # 每一行
            cell_str = self.ui.tableWidget.item(row_l, column_l).text()
            row_data.append(int(cell_str))
        # print(column_data)
        return row_data

    def set_item_data(self, row_num_1, column_num_1, row_num_2, column_num_2):
        item_1 = self.ui.tableWidget.item(row_num_1, column_num_1)
        item_2 = self.ui.tableWidget.item(row_num_2, column_num_2)
        int_1 = int(item_1.text())
        int_2 = int(item_2.text())
        if int_1 == int_2:
            item_2.setText(str(int_1 * 2))
            item_1.setText("0")
        else:
            if int_2 == 0:
                item_2.setText(str(int_1))
                item_1.setText("0")

    def sort_one_column_up(self, i):
        column_data = self.getcolumn_data(i)
        if column_data == [0, 0, 0, 0]:
            pass
        else:
            while True:
                length_column = len(column_data)
                while length_column > 1:
                    self.set_item_data(length_column - 1, i - 1, length_column - 2, i - 1)
                    length_column = length_column - 1
                column_data = self.getcolumn_data(i)
                if len(set(column_data)) == 4:
                    break
                if len(set(column_data[0:3])) == 3 and column_data[3] == 0:
                    break
                if len(set(column_data[0:2])) == 2 and column_data[2] == 0 and column_data[3] == 0:
                    break
                if column_data[1] == 0 and column_data[2] == 0 and column_data[3] == 0:
                    break
                if column_data[0] != column_data[1] and column_data[1] != column_data[2] and column_data[2] != column_data[3]:
                    break

    def sort_one_column_down(self, i):
        column_data = self.getcolumn_data(i)
        if column_data == [0, 0, 0, 0]:
            pass
        else:
            while True:
                length_column = len(column_data)
                times = 0
                while times < length_column - 1:
                    self.set_item_data(times, i - 1, times + 1, i - 1)
                    times = times + 1
                column_data = self.getcolumn_data(i)
                if len(set(column_data)) == 4:
                    break
                if len(set(column_data[1:4])) == 3 and column_data[0] == 0:
                    break
                if len(set(column_data[2:4])) == 2 and column_data[0] == 0 and column_data[1] == 0:
                    break
                if column_data[0] == 0 and column_data[1] == 0 and column_data[2] == 0:
                    break
                if column_data[0] != column_data[1] and column_data[1] != column_data[2] and column_data[2] != column_data[3]:
                    break

    def sort_one_column_left(self, i):
        row_data = self.getrow_data(i)
        if row_data == [0, 0, 0, 0]:
            pass
        else:
            while True:
                length_column = len(row_data)
                while length_column > 1:
                    self.set_item_data(i - 1, length_column - 1, i - 1, length_column - 2)
                    length_column = length_column - 1
                row_data = self.getrow_data(i)
                if len(set(row_data)) == 4:
                    break
                if len(set(row_data[0:3])) == 3 and row_data[3] == 0:
                    break
                if len(set(row_data[0:2])) == 2 and row_data[2] == 0 and row_data[3] == 0:
                    break
                if row_data[1] == 0 and row_data[2] == 0 and row_data[3] == 0:
                    break
                if row_data[0] != row_data[1] and row_data[1] != row_data[2] and row_data[2] != row_data[3]:
                    break

    def sort_one_column_right(self, i):
        row_data = self.getrow_data(i)
        if row_data == [0, 0, 0, 0]:
            pass
        else:
            while True:
                length_column = len(row_data)
                times = 0
                while times < length_column - 1:
                    self.set_item_data(i - 1, times, i - 1, times + 1)
                    times = times + 1
                row_data = self.getrow_data(i)
                if len(set(row_data)) == 4:
                    break
                if len(set(row_data[1:4])) == 3 and row_data[0] == 0:
                    break
                if len(set(row_data[2:4])) == 2 and row_data[0] == 0 and row_data[1] == 0:
                    break
                if row_data[0] == 0 and row_data[1] == 0 and row_data[2] == 0:
                    break
                if row_data[0] != row_data[1] and row_data[1] != row_data[2] and row_data[2] != row_data[3]:
                    break

    def default_color(self):
        for y in range(4):
            for z in range(4):
                cell_item = self.ui.tableWidget.item(y, z)
                cell_item.setBackground(QBrush(QColor(255, 255, 255)))

    def generate_randnum(self):
        self.default_color()
        new_element = 4 if random.randint(0, 100) > 89 else 2
        while True:
            x_pos = random.randint(0, 3)
            y_pos = random.randint(0, 3)
            item = self.ui.tableWidget.item(x_pos, y_pos)
            content = item.text()
            if content == "0":
                item.setText(str(new_element))
                item.setBackground(QBrush(QColor(195, 202, 203)))
                break

    def fail_judge(self):
        break_out = False
        for k in range(1, 5):
            data_cloumn = self.getcolumn_data(k)
            for m in range(4):
                if data_cloumn[m] == 0:
                    break_out = True
                    break
            if break_out:
                break
        if not break_out:
            # print("game over")
            return True
        else:
            self.generate_randnum()
            return False

    def pass_judge(self):
        break_out = False
        for k in range(1, 5):
            data_cloumn = self.getcolumn_data(k)
            for m in range(4):
                if data_cloumn[m] == 2048:
                    break_out = True
                    break
            if break_out:
                break
        if break_out:
            print("Success")
            self.game_pass = True
            self.ui.tableWidget.setVisible(False)
            self.ui.label.setVisible(True)
            self.ui.label_2.setVisible(True)
            self.ui.label_2.setText("You only spend {} count".format(self.count))
            self.ui.pushButton.setVisible(True)

    def up_excuted(self):
        self.count = self.count + 1
        if self.count == 5:
            self.ui.tableWidget.item(3, 0).setText(str(2048))
        if not self.game_pass and not self.game_over:
            for x in range(1, 5):
                self.sort_one_column_up(x)
            over_pa = self.fail_judge()
            if over_pa:
                self.up_game_over = True
            if self.up_game_over and self.down_game_over and self.left_game_over and self.right_game_over:
                self.game_over = True
                print("game over")
            self.pass_judge()

    def down_excuted(self):
        self.count = self.count + 1
        if not self.game_pass and not self.game_over:
            for x in range(1, 5):
                self.sort_one_column_down(x)
            over_pa = self.fail_judge()
            if over_pa:
                self.down_game_over = True
            if self.up_game_over and self.down_game_over and self.left_game_over and self.right_game_over:
                self.game_over = True
                print("game over")
            self.pass_judge()

    def left_excuted(self):
        self.count = self.count + 1
        if not self.game_pass and not self.game_over:
            for x in range(1, 5):
                self.sort_one_column_left(x)
            over_pa = self.fail_judge()
            if over_pa:
                self.left_game_over = True
            if self.up_game_over and self.down_game_over and self.left_game_over and self.right_game_over:
                self.game_over = True
                print("game over")
            self.pass_judge()

    def right_excuted(self):
        self.count = self.count + 1
        if not self.game_pass and not self.game_over:
            for x in range(1, 5):
                self.sort_one_column_right(x)
            over_pa = self.fail_judge()
            if over_pa:
                self.right_game_over = True
            if self.up_game_over and self.down_game_over and self.left_game_over and self.right_game_over:
                self.game_over = True
                print("game over")
            self.pass_judge()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())

#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : python-20201211 -> game_2048_optimize.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/1/9 13:51
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
            self.up_move()
        if event.key() == Qt.Key_A or event.key() == Qt.Key_Down:
            self.down_move()
        if event.key() == Qt.Key_S or event.key() == Qt.Key_Left:
            self.left_move()
        if event.key() == Qt.Key_D or event.key() == Qt.Key_Right:
            self.right_move()

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
        return row_data

    def remove_zero(self, aim_list):
        des_list = []
        for item in aim_list:
            if item != 0:
                des_list.append(item)
        if len(des_list) == len(aim_list):
            return des_list, False
        return des_list, True

    def merge_list(self, mer_list):
        temp_mer_list = mer_list
        length_temp = len(temp_mer_list)
        while length_temp > 1:
            if temp_mer_list[-1] == temp_mer_list[-2]:
                temp_mer_list[-2] = temp_mer_list[-2] * 2
                temp_mer_list[-1] = 0
            else:
                if temp_mer_list[-2] == 0:
                    temp_mer_list[-2] = temp_mer_list[-1]
                    temp_mer_list[-1] = 0
            length_temp = length_temp - 1
        return temp_mer_list

    def merge_list_reversed(self, mer_list):
        temp_mer_list = mer_list
        length_temp = len(temp_mer_list)
        times = 0
        while times < length_temp - 1:
            if temp_mer_list[times] == temp_mer_list[times + 1]:
                temp_mer_list[times + 1] = temp_mer_list[times] * 2
                temp_mer_list[times] = 0
            else:
                if temp_mer_list[times + 1] == 0:
                    temp_mer_list[times + 1] = temp_mer_list[times]
                    temp_mer_list[times] = 0
            times = times + 1
        return temp_mer_list

    def paint_column(self, data_column, column_num):
        for row_num in range(len(data_column)):
            item = self.ui.tableWidget.item(row_num, column_num - 1)
            item.setText(str(data_column[row_num]))

    def paint_row(self, data_row, row_num):
        print(row_num)
        for column_num in range(len(data_row)):
            item = self.ui.tableWidget.item(row_num - 1, column_num)
            item.setText(str(data_row[column_num]))

    def sort_one_column_up(self, colum_num):
        column_data = self.getcolumn_data(colum_num)
        temp_data = column_data
        break_out = False
        while not break_out:
            temp_data, modify = self.remove_zero(temp_data)
            if len(temp_data) == 0:
                break_out = True
            elif modify is False:
                repeat_data = False
                for a in range(len(temp_data) - 1):
                    if temp_data[a] == temp_data[a+1]:
                        repeat_data = True
                        break
                if not repeat_data:
                    break_out = True
            else:
                temp_data = self.merge_list(temp_data)
        num_zero = len(column_data) - len(temp_data)
        for x in range(num_zero):
            temp_data.append(0)
        self.paint_column(temp_data, colum_num)

    def sort_one_column_down(self, colum_num):
        column_data = self.getcolumn_data(colum_num)
        temp_data = column_data
        break_out = False
        while not break_out:
            temp_data, modify = self.remove_zero(temp_data)
            if len(temp_data) == 0:
                break_out = True
            elif modify is False:
                repeat_data = False
                for a in range(len(temp_data) - 1):
                    if temp_data[a] == temp_data[a+1]:
                        repeat_data = True
                        break
                if not repeat_data:
                    break_out = True
            else:
                temp_data = self.merge_list_reversed(temp_data)
        num_zero = len(column_data) - len(temp_data)
        for x in range(num_zero):
            temp_data.insert(0, 0)
        self.paint_column(temp_data, colum_num)

    def sort_one_column_left(self, row_num):
        row_data = self.getrow_data(row_num)
        temp_data = row_data
        break_out = False
        while not break_out:
            temp_data, modify = self.remove_zero(temp_data)
            if len(temp_data) == 0:
                break_out = True
            elif modify is False:
                repeat_data = False
                for a in range(len(temp_data) - 1):
                    if temp_data[a] == temp_data[a+1]:
                        repeat_data = True
                        break
                if not repeat_data:
                    break_out = True
            else:
                temp_data = self.merge_list(temp_data)
        num_zero = len(row_data) - len(temp_data)
        for x in range(num_zero):
            temp_data.append(0)
        self.paint_row(temp_data, row_num)

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

    def up_move(self):
        self.count = self.count + 1
        # if self.count == 5:
        #     self.ui.tableWidget.item(3, 0).setText(str(2048))
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

    def down_move(self):
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

    def left_move(self):
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

    def right_move(self):
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


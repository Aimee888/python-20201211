#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : python-20201211 -> game_2048_update.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/1/9 13:51
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QBrush, QColor, QFont
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

        self.game_pass = False  # 游戏通关
        self.game_fail = False  # 游戏失败
        self.count = 0  # 移动的步数
        self.random_genarate = 0  # 当value = 4时不产生随机数

    # 初始化设置
    def init_setting(self):
        # 隐藏行表头
        self.ui.tableWidget.horizontalHeader().hide()
        self.ui.tableWidget.verticalHeader().hide()
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

    # 初始化数据
    def init_datas(self):
        self.generate_randnum()
        self.generate_randnum()

    # 接收键盘消息
    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_W or event.key() == Qt.Key_Up:
            self.move_function("up")
        if event.key() == Qt.Key_A or event.key() == Qt.Key_Down:
            self.move_function("down")
        if event.key() == Qt.Key_S or event.key() == Qt.Key_Left:
            self.move_function("left")
        if event.key() == Qt.Key_D or event.key() == Qt.Key_Right:
            self.move_function("right")

    # 获取1列数据
    def getcolumn_data(self, num_column):
        column_l = num_column - 1
        column_data = []
        for row_l in range(4):  # 每一行
            cell_str = self.ui.tableWidget.item(row_l, column_l).text()
            column_data.append(int(cell_str))
        # print(column_data)
        return column_data

    # 获取1行数据
    def getrow_data(self, num_row):
        row_l = num_row - 1
        row_data = []
        for column_l in range(4):  # 每一行
            cell_str = self.ui.tableWidget.item(row_l, column_l).text()
            row_data.append(int(cell_str))
        return row_data

    # 更新1列数据
    def paint_column(self, data_column, column_num):
        for row_num in range(len(data_column)):
            item = self.ui.tableWidget.item(row_num, column_num - 1)
            item.setText(str(data_column[row_num]))

    # 更新1行数据
    def paint_row(self, data_row, row_num):
        for column_num in range(len(data_row)):
            item = self.ui.tableWidget.item(row_num - 1, column_num)
            item.setText(str(data_row[column_num]))

    def remove_zero(self, del_zero_list):
        new_list = []
        for i in del_zero_list:
            if i != 0:
                new_list.append(i)
        return new_list

    # 正向合并数据
    def get_sort_list(self, aim_list):
        temp_list = aim_list[:]  # 使用切片方式赋值可以防止列表改变
        length_list = len(temp_list)
        # 去0
        temp_list = self.remove_zero(temp_list)
        # 排序
        temp_length = len(temp_list)
        for j in range(temp_length - 1):
            if temp_list[j] == temp_list[j+1]:
                temp_list[j+1] = temp_list[j+1] * 2
                temp_list[j] = 0
                break
        # while temp_length > 1:
        #     if temp_list[temp_length - 1] == temp_list[temp_length - 2]:
        #         temp_list[temp_length - 2] = temp_list[temp_length - 2] * 2
        #         temp_list[temp_length - 1] = 0
        #         break
        #     temp_length = temp_length - 1
        # 去0
        temp_list = self.remove_zero(temp_list)
        # 补0
        for k in range(length_list - len(temp_list)):
            temp_list.append(0)
        if temp_list == aim_list:
            self.random_genarate = self.random_genarate + 1
        return temp_list

    def get_sort_list_reverse(self, aim_list):
        temp_list = aim_list[:]  # 使用切片方式赋值可以防止列表改变
        length_list = len(temp_list)
        # 去0
        temp_list = self.remove_zero(temp_list)
        # 排序
        temp_length = len(temp_list)
        while temp_length > 1:
            if temp_list[temp_length - 1] == temp_list[temp_length - 2]:
                temp_list[temp_length - 2] = temp_list[temp_length - 2] * 2
                temp_list[temp_length - 1] = 0
                break
            temp_length = temp_length - 1
        # for j in range(temp_length - 1):
        #     if temp_list[j] == temp_list[j+1]:
        #         temp_list[j+1] = temp_list[j+1] * 2
        #         temp_list[j] = 0
        #         break
        # 去0
        temp_list = self.remove_zero(temp_list)
        # 补0
        for k in range(length_list - len(temp_list)):
            temp_list.insert(0, 0)
        if temp_list == aim_list:
            self.random_genarate = self.random_genarate + 1
        return temp_list

    def draw_tablewidgt(self, subscipt, direction="up"):
        if direction == "up":
            column_list = self.getcolumn_data(subscipt)
            final_list = self.get_sort_list(column_list)
            self.paint_column(final_list, subscipt)
        elif direction == "down":
            column_list = self.getcolumn_data(subscipt)
            final_list = self.get_sort_list_reverse(column_list)
            self.paint_column(final_list, subscipt)
        elif direction == "left":
            row_list = self.getrow_data(subscipt)
            final_list = self.get_sort_list(row_list)
            self.paint_row(final_list, subscipt)
        elif direction == "right":
            row_list = self.getrow_data(subscipt)
            final_list = self.get_sort_list_reverse(row_list)
            self.paint_row(final_list, subscipt)
        else:
            pass

    # QTableWidgt恢复默认颜色
    def default_color(self):
        for y in range(4):
            for z in range(4):
                item = self.ui.tableWidget.item(y, z)
                self.get_color(int(item.text()), item)

    def get_color(self, number, cell_item):
        if number == 0:
            brush = QBrush(QColor(216, 216, 216))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            cell_item.setBackground(brush)
        elif number == 2:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(255, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 4:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(255, 255, 204))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 8:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(255, 204, 153))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 16:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(255, 153, 102))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 32:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(255, 153, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 64:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(255, 102, 102))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 128:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(204, 255, 255))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 256:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(153, 204, 255))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 512:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(102, 204, 153))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 1024:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(153, 204, 102))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)
        elif number == 2048:
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setForeground(brush)
            brush = QBrush(QColor(153, 204, 204))
            brush.setStyle(Qt.SolidPattern)
            cell_item.setBackground(brush)

    # 产生随机数
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
                self.get_color(new_element, item)
                break

    # 判断游戏是否失败 -- 不能移动
    def fail_judge(self):
        for x in range(1, 5):
            row = self.getrow_data(x)
            column = self.getcolumn_data(x)
            for y in range(4):
                if row[y] == 0 or column[y] == 0:
                    return False
                if y < 3:
                    if row[y] == row[y+1] or column[y] == column[y + 1]:
                        return False
        self.game_fail = True
        return True

    # 判断游戏是否成功--有无2048
    def pass_judge(self):
        for k in range(1, 5):
            data_cloumn = self.getcolumn_data(k)
            for m in range(4):
                if data_cloumn[m] == 2048:
                    self.game_pass = True
                    return True
        return False

    def fail_funtion(self):
        self.ui.tableWidget.setVisible(False)
        self.ui.label.setVisible(True)
        self.ui.label.setText("Game Over!!!")
        self.ui.label_2.setVisible(True)
        self.ui.label_2.setText("You spend {} count".format(self.count))
        self.ui.pushButton.setVisible(True)

    # 成功后刷新界面
    def pass_funtion(self):
        self.ui.tableWidget.setVisible(False)
        self.ui.label.setVisible(True)
        self.ui.label_2.setVisible(True)
        self.ui.label_2.setText("You only spend {} count".format(self.count))
        self.ui.pushButton.setVisible(True)

    def move_init(self):
        self.count = self.count + 1
        self.random_genarate = 0
        self.default_color()

    def move_function(self, direct):
        if not self.game_pass and not self.game_fail:
            self.move_init()
            for x in range(1, 5):
                self.draw_tablewidgt(x, direct)
            if self.random_genarate < 4:
                self.generate_randnum()
            self.fail_judge()
            if self.game_fail:
                print("game over")
                self.fail_funtion()
            self.pass_judge()
            if self.game_pass:
                print("successful")
                self.pass_funtion()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())


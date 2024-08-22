import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        self.target_dic, self.source_dict, self.source_list = get()
        data = []
        for key in self.source_list:
            temp = [key]
            temp.append(self.source_dict.get(key))
            temp.append(self.target_dic.get(key))
            data.append(temp)
        self.init_table(data)

        save = QPushButton("Save")
        close = QPushButton("Close")
        close.clicked.connect(self.close)
        save.clicked.connect(self.save_lang)

        grid.addWidget(self.table_view, 1, 1, 1, 2)
        grid.addWidget(save, 2, 1)
        grid.addWidget(close, 2, 2)

        self.setLayout(grid)
        self.resize(800, 500)
        self.center()

        self.setWindowTitle('TransTool')
        self.show()

    def init_table(self, data):
        self.model = QStandardItemModel(len(data), 3)
        self.model.setHorizontalHeaderLabels(["KEY", source, target])
        for i in range(len(data)):
            k = QStandardItem(data[i][0])
            k.setEditable(False)
            self.model.setItem(i, 0, k)
            s = QStandardItem(data[i][1])
            s.setEditable(False)
            self.model.setItem(i, 1, s)
            self.model.setItem(i, 2, QStandardItem(data[i][2]))
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

    def save_lang(self):
        # save the new lang
        wait_save_list = {}
        for i in range(self.model.rowCount()):
            wait_save_list[self.model.itemFromIndex(
                self.model.index(i, 0)).text()] = self.model.itemFromIndex(
                self.model.index(i, 2)).text()

        with open(path + "new_" + target, encoding="UTF8", mode="w") as f, open(path + source, encoding="UTF8", mode="r") as sf:
            for lines in sf.readlines():
                if '=' in lines:
                    key = lines.split("=")[0]
                    if len(wait_save_list[key].strip()) != 0:
                        f.writelines(
                            key + "=" + wait_save_list[key].strip() + "\n")
                    else:
                        # default skip null
                        # f.writelines(lines)
                        ...
                else:
                    f.writelines(lines)
            sf.close()
            f.close()
        print("Saveing complete")

    def switch_filter(self):
        # TODO add row filter for showing all none translated item
        ...

    def center(self):
        # for move window to center of screen
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    win = window()
    sys.exit(app.exec())


def get():
    target_dic = {}
    with open(path + target, encoding="UTF8") as file:
        for lines in file.readlines():
            if '=' in lines:
                target_dic[lines.split("=")[0]] = lines.split("=")[1].strip()
        file.close()

    source_list = []
    source_dict = {}
    with open(path + source, encoding="UTF8") as file:
        for lines in file.readlines():
            if '=' in lines:
                source_dict[lines.split("=")[0]] = lines.split("=")[1].strip()
                source_list.append(lines.split("=")[0])
        file.close()

    return target_dic, source_dict, source_list


if __name__ == "__main__":
    path = input("Please input path of lang \n") + "\\"
    source = input("Please input the souse lang(without .lang)\n") + ".lang"
    target = input(
        "Please input the target lang(without .lang) or just input all for others\n") + ".lang"
    main()

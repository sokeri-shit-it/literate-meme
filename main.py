import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QButtonGroup
from untitled1 import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("films_db.sqlite")
        self.modified = {}
        self.titles = None
        self.result = None
        self.pushButton.clicked.connect(self.click)
        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        for i in range(2, 33):
            self.button = getattr(self, 'pushButton_%s' % i)
            self.btn_grp.addButton(self.button)
            self.button.setCheckable(True)

        self.btn_grp.buttonClicked.connect(self.click)

    def click(self):
        cur = self.con.cursor()
        self.statusBar().showMessage(self.sender().text())
        self.result = cur.execute(f"""SELECT * FROM films where title like 
                                        '{self.sender().text()}%'""").fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(self.result))
        # Если запись не нашлась, то не будем ничего делат
        self.tableWidget.setColumnCount(len(self.result[0]))
        print(self.sender().text())
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Жанр', 'Год', 'Продолжительность'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

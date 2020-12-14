import sys
import sqlite3
from sqlite3 import Error

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from films_wid import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("films_db.sqlite")
        self.titles = None
        self.pushButton.clicked.connect(self.click)

    def click(self):
        try:
            cur = self.con.cursor()
            result = cur.execute(
                f"""select * from films where genre in(select id from genres where title='{self.comboBox.currentText()}')""").fetchall()
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in result]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        except Error as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

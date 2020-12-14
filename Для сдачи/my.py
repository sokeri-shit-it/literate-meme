import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled1 import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click)

    def click(self):
        temp1 = int(self.lineEdit.text())
        temp2 = int(self.lineEdit_2.text())
        sum_nums = temp1 + temp2
        self.lcdNumber.display(sum_nums)
        dif_nums = temp1 - temp2
        self.lcdNumber_2.display(dif_nums)
        comp_nums = temp1 * temp2
        self.lcdNumber_4.display(comp_nums)
        if temp2 == 0:
            self.lcdNumber_3.display('Error')
        else:
            freq_nums = temp1 / temp2
            self.lcdNumber_3.display(freq_nums)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

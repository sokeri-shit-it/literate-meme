import sys
import sqlite3
import os
import psutil
import magic
import glob
from sqlite3 import Error
from datetime import datetime

from pathlib import Path
from humanize import naturalsize
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QMessageBox, QFileDialog

from file_analyzer import Ui_project_admin


class MyAnalyzer(QMainWindow, Ui_project_admin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.modified = {}
        self.titles = None
        self.titles_sort = None
        self.result = None
        self.result_sort = None
        self.fold_size = None
        self.dir_folder = None

        self.con_history = sqlite3.connect('history_analyzer.sqlite')
        self.con_folder = sqlite3.connect('folder_sort.sqlite')
        self.con_file = sqlite3.connect('file_sort.sqlite')
        self.cur_history = self.con_history.cursor()
        self.cur_folder = self.con_folder.cursor()
        self.cur_file = self.con_file.cursor()
        self.start.clicked.connect(self.analyze_file)
        self.cur_folder.execute("""delete from folder""")
        self.cur_folder.execute("""DELETE FROM SQLite_sequence WHERE name = 'folder'""")
        self.con_folder.commit()
        self.con_folder.commit()
        self.cur_folder.execute("""delete from disk""")
        self.cur_folder.execute("""DELETE FROM SQLite_sequence WHERE name = 'disk'""")
        self.con_folder.commit()
        self.con_folder.commit()
        self.cur_file.execute("""delete from analyze""")
        self.cur_file.execute("""DELETE FROM SQLite_sequence WHERE name = 'analyze'""")
        self.con_file.commit()
        self.con_file.commit()

    def analyze_file(self):
        if self.folder.isChecked():
            self.dir_folder = QFileDialog.getExistingDirectory(self, "Выбрать папки", ".")

            if self.dir_folder == '':
                self.statusBar().showMessage(
                    f'Простите, но вы не выбрали папку. Пожлуйста выберете ее снова.')

            elif self.dir_folder == 'C:/':
                self.statusBar().showMessage(
                    f'Простите но вы выбрали диск {self.dir_folder}. Выберете пожалуйста папку.')

            else:
                norm_name = os.path.basename(self.dir_folder)
                self.fold_size = naturalsize(sum(file.stat().st_size for file in Path(self.dir_folder).rglob('*')))

                self.info.setText(
                    f'Была выбрана папка \'{norm_name}\'. Общая загруженность папки состовляет {self.fold_size}')

                files = glob.glob(self.dir_folder + '*')
                try:
                    for i in files:
                        name = os.path.basename(i)
                        print(name)
                        if os.path.isfile(i):
                            size = naturalsize(os.path.getsize(i))
                            self.cur_history.execute(
                                f"""insert into history(data, folder_name, workload, objects) values(
                                                            "{datetime.now().date()}", "{name}", "{size}", "-")""")
                            self.con_history.commit()

                            self.cur_folder.execute(f"""insert into folder(file_name, usage, objects) values(
                                                                "{name}", "{size}", "-")""")
                            self.con_folder.commit()
                        else:
                            ob = len(os.listdir(i))
                            if len(os.listdir(i)) == 0:
                                size = 0
                                self.cur_history.execute(
                                    f"""insert into history(data, folder_name, workload, objects) values(
                                                    "{datetime.now().date()}", "{name}", "{size}", {'0'})""")
                                self.con_history.commit()

                                self.cur_folder.execute(f"""insert into folder(file_name, usage, objects) values(
                                                                                "{name}", "{size}", {'0'})""")
                                self.con_folder.commit()
                            else:
                                size = naturalsize(sum(file.stat().st_size for file in Path(i).rglob('*')))

                                self.cur_history.execute(
                                    f"""insert into history(data, folder_name, workload, objects) values(
                                            "{datetime.now().date()}", "{name}", "{str(size)}", "{str(ob)}")""")
                                self.con_history.commit()

                                self.cur_folder.execute(f"""insert into folder(file_name, usage, objects) values(
                                                                    "{name}", "{str(size)}", "{str(ob)}")""")
                                self.con_folder.commit()
                                for file in Path(i).rglob('*'):
                                    norm_f = os.path.basename(file)
                                    if os.path.isfile(file):
                                        size_f = naturalsize(os.path.getsize(file))
                                        self.cur_history.execute(
                                            f"""insert into history(data, folder_name, workload, objects) values(
                                        "{datetime.now().date()}", "{norm_f}", "{str(size_f)}", "-")""")
                                        self.con_history.commit()

                                        self.cur_folder.execute(f"""insert into folder(file_name, usage, objects) 
                                                        values("{norm_f}", "{str(size_f)}", "-")""")

                                        self.con_folder.commit()

                    self.result = self.cur_folder.execute("""select * from folder""").fetchall()

                    self.tableWidget_2.setRowCount(len(self.result))
                    self.tableWidget_2.setColumnCount(len(self.result[0]))
                    self.tableWidget_2.setHorizontalHeaderLabels(
                        ['ID', 'Имя папки/файла', 'Загруженость', 'Кол-во объектов'])
                    header = self.tableWidget_2.horizontalHeader()
                    header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(1, QHeaderView.Stretch)
                    header.setSectionResizeMode(2, QHeaderView.Stretch)
                    header.setSectionResizeMode(3, QHeaderView.Stretch)
                    self.titles = [description[0] for description in self.result]

                    for i, elem in enumerate(self.result):
                        for j, val in enumerate(elem):
                            self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))
                    self.modified = {}

                    self.cur_folder.execute("""delete from folder""")
                    self.con_folder.commit()

                except Error as e:
                    raise e

        elif self.disk_media.isChecked():
            self.dir_folder = QFileDialog.getExistingDirectory(self, "Выбрать папки", 'C:/')

            if self.dir_folder == '':
                self.statusBar().showMessage(
                    f'Простите, но вы не выбрали диск. Пожлуйста выберете его снова.')

            else:
                free = psutil.disk_usage(self.dir_folder).free / (1024 * 1024 * 1024)
                total = psutil.disk_usage(self.dir_folder).total / (1024 * 1024 * 1024)
                pr_total = int(100 - (free / total) * 100)
                files = os.listdir(self.dir_folder)

                try:
                    self.cur_history.execute(f"""insert into disk_desk(data, name, work_load, usage, objects) values(
                                            "{datetime.now().date()}", '{self.dir_folder}', '{(str(f'{pr_total}%'))}', 
                                                "{str(f'{int(total - free)} Gb')}", {len(files)})""")
                    self.con_history.commit()

                    self.cur_folder.execute(f"""insert into disk(disk_name, workload, usage, objects) values(
                                                '{self.dir_folder}', '{(str(f'{pr_total}%'))}', 
                                                "{str(f'{int(total - free)} Gb')}", {len(files)})""")
                    self.con_folder.commit()

                    self.result = self.cur_folder.execute(f"""select * from disk""").fetchall()
                    self.tableWidget_2.setRowCount(len(self.result))
                    self.tableWidget_2.setColumnCount(len(self.result[0]))
                    self.tableWidget_2.setHorizontalHeaderLabels(
                        ['ID', 'Имя файла', 'Загруженость', 'Использование', 'Кол-во объектов'])
                    header = self.tableWidget_2.horizontalHeader()
                    header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(1, QHeaderView.Stretch)
                    header.setSectionResizeMode(2, QHeaderView.Stretch)
                    header.setSectionResizeMode(3, QHeaderView.Stretch)
                    header.setSectionResizeMode(4, QHeaderView.Stretch)
                    self.titles = [description[0] for description in self.result]

                    for i, elem in enumerate(self.result):
                        for j, val in enumerate(elem):
                            self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))
                    self.modified = {}

                    self.cur_folder.execute("""delete from disk""")
                    self.con_folder.commit()

                except Error as e:
                    print(e)

        elif self.file.isChecked():
            self.dir_folder, file_type = QFileDialog.getOpenFileName(self, 'Выбор файла')
            print(self.dir_folder)

            if self.dir_folder == '':
                self.statusBar().showMessage(
                    f'Простите, но вы не выбрали файл. Пожлуйста выберете его снова.')

            else:
                file_size = os.path.getsize(self.dir_folder)

                norm_name = os.path.basename(self.dir_folder)
                file_type = magic.from_file(self.dir_folder, mime=True)

                try:
                    self.cur_history.execute(
                        f"""insert into file_history(data, file_name, usage, type) values("{datetime.now().date()}", 
                            "{norm_name}", "{file_size}", "{file_type}")""")
                    self.con_history.commit()

                    self.cur_file.execute(
                        f"""insert into analyze(name, usage, type) values("{norm_name}", 
                                                        "{file_size}", "{file_type}")""")
                    self.con_file.commit()

                    self.result = self.cur_file.execute("""select * from analyze""").fetchall()

                    self.tableWidget_2.setRowCount(len(self.result))
                    self.tableWidget_2.setColumnCount(len(self.result[0]))
                    self.tableWidget_2.setHorizontalHeaderLabels(['ID', 'Имя файла', 'Загруженость', 'Тип файла'])
                    header = self.tableWidget_2.horizontalHeader()
                    header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(1, QHeaderView.Stretch)
                    header.setSectionResizeMode(2, QHeaderView.Stretch)
                    header.setSectionResizeMode(3, QHeaderView.Stretch)
                    self.titles = [description[0] for description in self.result]

                    for i, elem in enumerate(self.result):
                        for j, val in enumerate(elem):
                            self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(val)))
                    self.modified = {}

                    self.cur_file.execute("""delete from analyze""")
                    self.con_file.commit()

                except Error as e:
                    self.statusBar().showMessage(str(e))
                    print(e)


class History(MyAnalyzer):
    def __init__(self):
        super().__init__()
        self.sort.clicked.connect(self.sort_db)
        self.drop_filt.clicked.connect(self.clear_filter)
        self.delete_all.clicked.connect(self.clear_recorded)

    def sort_db(self):
        print(self.comboBox.currentIndex())
        try:
            if self.comboBox.currentIndex() == 0:
                self.result = self.cur_history.execute(f"""SELECT * FROM history""").fetchall()
                if self.sort_to_new.currentIndex() == 0 and not self.fol_name.text() and self.sort_to_new.isEnabled():
                    self.result = self.cur_history.execute(f"""SELECT * from history order by data asc""").fetchall()
                    print('test1')

                elif self.sort_to_new.currentIndex() == 1 and not self.fol_name.text():
                    self.result = self.cur_history.execute(f"""SELECT * FROM history order by data desc""").fetchall()
                    print('test2')

                elif self.sort_to_new.currentIndex() == 0 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from history where folder_name like 
                                                '{self.fol_name.text()}%' order by data asc""").fetchall()
                    print('test3')

                elif self.sort_to_new.currentIndex() == 1 and self.fol_name.text():
                    self.result = self.cur_history.execute(
                        f"""select * from history where folder_name like 
                            '{self.fol_name.text()}%' order by data desc""").fetchall()
                    print('test4')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 0\
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from history order by data asc, workload asc""").fetchall()
                    print('t5')

                elif self.work.currentIndex() == 1 and self.sort_to_new.currentIndex() == 1\
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from history order by data desc, workload desc""").fetchall()
                    print('t6')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex()\
                        == 1 and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from history order by data asc, workload desc""").fetchall()
                    print('t7')

                elif self.work.currentIndex() == 1 and self.sort_to_new.currentIndex() == 0 \
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from history order by data desc, workload asc""").fetchall()
                    print('t7')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 0\
                        and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from history where folder_name like 
                                {self.fol_name.text()} order by data, workload""").fetchall()
                    print('t8')

                elif self.work.currentIndex() == 1 and self.sort_to_new.currentIndex() == 1\
                        and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from history where folder_name like 
                                {self.fol_name.text()} order by data desc, workload desc""").fetchall()
                    print('t9')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 1\
                        and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from history where folder_name like 
                                {self.fol_name.text()} order by data, workload desc""").fetchall()
                    print('t10')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 1\
                        and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from history where folder_name like 
                                {self.fol_name.text()} order by data desc, workload asc""").fetchall()
                    print('t11')

            if self.comboBox.currentIndex() == 1:
                self.result = self.cur_history.execute(f"""SELECT * FROM file_history""").fetchall()

                if self.sort_to_new.currentIndex() == 0 and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        f"""SELECT * from file_history order by data asc""").fetchall()
                    print('test1')

                elif self.sort_to_new.currentIndex() == 1 and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        f"""SELECT * FROM file_history order by data desc""").fetchall()
                    print('test2')

                elif self.sort_to_new.currentIndex() == 0 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from file_history where file_name like 
                                                '{self.fol_name.text()}%' order by data asc""").fetchall()
                    print('test3')

                elif self.sort_to_new.currentIndex() == 1 and self.fol_name.text():
                    self.result = self.cur_history.execute(
                        f"""select * from file_history where file_name like 
                            '{self.fol_name.text()}%' order by data desc""").fetchall()
                    print('test4')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 0 \
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from file_history order by data asc, usage asc""").fetchall()
                    print('t5')

                elif self.work.currentIndex() == 1 and self.sort_to_new.currentIndex() == 1 \
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from file_history order by data desc, usage desc""").fetchall()
                    print('t6')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 1 \
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from file_history order by data asc, usage desc""").fetchall()
                    print('t7')

                elif self.work.currentIndex() == 1 and self.sort_to_new.currentIndex() \
                        == 0 and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from file_history order by data desc, usage asc""").fetchall()
                    print('t7')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 0 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from file_history where file_name like 
                                {self.fol_name.text()} order by data, usage""").fetchall()
                    print('t8')

                elif self.work.currentIndex() == 1 and self.sort_to_new.currentIndex() == 1 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from file_history where file_name like 
                                {self.fol_name.text()} order by data desc, usage desc""").fetchall()
                    print('t9')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 1 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from file_history where file_name like 
                                {self.fol_name.text()} order by data, usage desc""").fetchall()
                    print('t10')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 1 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from file_history where file_name like 
                                {self.fol_name.text()} order by data desc, usage asc""").fetchall()
                    print('t11')

            elif self.comboBox.currentIndex() == 2:
                self.result = self.cur_history.execute(f"""SELECT * FROM disk_desk""").fetchall()
                if self.sort_to_new.currentIndex() == 0 and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        f"""SELECT * from disk_desk order by data asc""").fetchall()
                    print('test1')

                elif self.sort_to_new.currentIndex() == 1 and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        f"""SELECT * FROM disk_desk order by data desc""").fetchall()
                    print('test2')

                elif self.sort_to_new.currentIndex() == 0 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from disk_desk where folder_name like 
                                                        '{self.fol_name.text()}%' order by data asc""").fetchall()
                    print('test3')

                elif self.sort_to_new.currentIndex() == 1 and self.fol_name.text():
                    self.result = self.cur_history.execute(
                        f"""select * from disk_desk where folder_name like 
'{self.fol_name.text()}%' order by data desc""") \
                        .fetchall()
                    print('test4')

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 0\
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from disk_desk order by data asc, workload asc""").fetchall()

                elif self.work.currentIndex() == 1 and self.sort_to_new.currentIndex() == 1\
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from disk_desk order by data desc, workload desc""").fetchall()

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 1\
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from disk_desk order by data asc, workload desc""").fetchall()

                elif self.work.currentIndex() == 1 and self.sort_to_new.currentIndex() == 0\
                        and not self.fol_name.text():
                    self.result = self.cur_history.execute(
                        """select * from disk_desk order by data desc, workload asc""").fetchall()

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 0 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from disk_desk where folder_name like 
                                        {self.fol_name.text()} order by data, workload""").fetchall()

                elif self.work.currentIndex() == 1 and self.sort_to_new.currentIndex() == 1 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from disk_desk where folder_name like 
                                        {self.fol_name.text()} order by data desc, workload desc""").fetchall()

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 1 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from disk_desk where folder_name like 
                                        {self.fol_name.text()} order by data, workload desc""").fetchall()

                elif self.work.currentIndex() == 0 and self.sort_to_new.currentIndex() == 1 and self.fol_name.text():
                    self.result = self.cur_history.execute(f"""select * from disk_desk where folder_name like 
                                        {self.fol_name.text()} order by data desc, workload asc""").fetchall()

            if not self.result:
                self.statusBar().showMessage('Простите но в данной таблице нет данных')

            else:
                self.statusBar().showMessage(f'Нашлось записей: {len(self.result)}')
                self.tableWidget.setRowCount(len(self.result))

                self.tableWidget.setColumnCount(len(self.result[0]))
                self.tableWidget.setHorizontalHeaderLabels(
                    ['ID', 'Дата', 'Название', 'Загруженость', 'Кол-во объектов'])
                header = self.tableWidget.horizontalHeader()
                header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
                header.setSectionResizeMode(1, QHeaderView.Stretch)
                header.setSectionResizeMode(2, QHeaderView.Stretch)
                header.setSectionResizeMode(3, QHeaderView.Stretch)
                header.setSectionResizeMode(4, QHeaderView.Stretch)
                self.titles = [description[0] for description in self.result]

                for i, elem in enumerate(self.result):
                    for j, val in enumerate(elem):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                self.modified = {}

        except Error as e:
            print(e)

    def clear_filter(self):
        self.fol_name.clear()
        self.work.setCurrentIndex(0)
        self.sort_to_new.setCurrentIndex(0)

    def clear_recorded(self):
        valid = QMessageBox.question(self, '', 'Вы действительно хотите удалить всю историю поиска?',
                                     QMessageBox.Yes, QMessageBox.No)

        if valid == QMessageBox.Yes:
            try:
                if self.comboBox.currentIndex() == 0:
                    self.cur_history.execute("""delete from history""")
                    self.cur_history.execute("""DELETE FROM SQLite_sequence WHERE name = 'history'""")
                    self.con_history.commit()

                elif self.comboBox.currentIndex() == 1:
                    self.cur_history.execute("""delete from file_history""")
                    self.cur_history.execute("""DELETE FROM SQLite_sequence WHERE name = 'file_history'""")
                    self.con_history.commit()

                elif self.comboBox.currentIndex() == 2:
                    self.cur_history.execute("""delete from disk_desk""")
                    self.cur_history.execute("""DELETE FROM SQLite_sequence WHERE name = 'disk_desk'""")
                    self.con_history.commit()
                self.statusBar().showMessage('Все записи удалены')
            except Error as e:
                print(e)


class PrintAbout(History):
    def __init__(self):
        super().__init__()
        self.file_config = 'config.txt'
        self.show_about.clicked.connect(self.file_work)

    def file_work(self):
        with open(self.file_config, 'r', encoding='utf-8') as f:
            self.textEdit.setText(f.read())


class PrintWidget(PrintAbout):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PrintWidget()
    ex.show()
    sys.exit(app.exec_())

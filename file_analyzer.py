# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_analyzer.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_project_admin(object):
    def setupUi(self, project_admin):
        project_admin.setObjectName("project_admin")
        project_admin.resize(852, 699)
        self.tabWidget = QtWidgets.QTabWidget(project_admin)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 851, 731))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 831, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.folder = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.folder.setFont(font)
        self.folder.setObjectName("folder")
        self.horizontalLayout.addWidget(self.folder)
        self.line_4 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.disk_media = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.disk_media.setFont(font)
        self.disk_media.setObjectName("disk_media")
        self.horizontalLayout.addWidget(self.disk_media)
        self.line_6 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout.addWidget(self.line_6)
        self.file = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.file.setObjectName("file")
        self.horizontalLayout.addWidget(self.file)
        self.start = QtWidgets.QPushButton(self.tab)
        self.start.setGeometry(QtCore.QRect(0, 110, 841, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 140, 851, 30))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.info = QtWidgets.QLabel(self.tab)
        self.info.setGeometry(QtCore.QRect(10, 160, 831, 21))
        self.info.setText("")
        self.info.setObjectName("info")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 190, 831, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(360, 0, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(0, 30, 851, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_7 = QtWidgets.QFrame(self.tab)
        self.line_7.setGeometry(QtCore.QRect(0, 80, 851, 30))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line.raise_()
        self.horizontalLayoutWidget.raise_()
        self.start.raise_()
        self.info.raise_()
        self.tableWidget_2.raise_()
        self.label_2.raise_()
        self.line_2.raise_()
        self.line_7.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sort_to_new = QtWidgets.QComboBox(self.tab_2)
        self.sort_to_new.setGeometry(QtCore.QRect(10, 50, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sort_to_new.setFont(font)
        self.sort_to_new.setObjectName("sort_to_new")
        self.sort_to_new.addItem("")
        self.sort_to_new.addItem("")
        self.fol_name = QtWidgets.QLineEdit(self.tab_2)
        self.fol_name.setGeometry(QtCore.QRect(10, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fol_name.setFont(font)
        self.fol_name.setObjectName("fol_name")
        self.drop_filt = QtWidgets.QPushButton(self.tab_2)
        self.drop_filt.setGeometry(QtCore.QRect(210, 150, 291, 41))
        self.drop_filt.setObjectName("drop_filt")
        self.delete_all = QtWidgets.QPushButton(self.tab_2)
        self.delete_all.setGeometry(QtCore.QRect(210, 100, 291, 41))
        self.delete_all.setObjectName("delete_all")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 230, 821, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.sort = QtWidgets.QPushButton(self.tab_2)
        self.sort.setGeometry(QtCore.QRect(210, 50, 291, 41))
        self.sort.setObjectName("sort")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_2)
        self.calendarWidget.setGeometry(QtCore.QRect(510, 10, 331, 201))
        self.calendarWidget.setObjectName("calendarWidget")
        self.work = QtWidgets.QComboBox(self.tab_2)
        self.work.setGeometry(QtCore.QRect(10, 150, 161, 41))
        self.work.setEditable(False)
        self.work.setObjectName("work")
        self.work.addItem("")
        self.work.addItem("")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 200, 491, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.show_admin_info = QtWidgets.QPushButton(self.tab_3)
        self.show_admin_info.setGeometry(QtCore.QRect(10, 10, 821, 31))
        self.show_admin_info.setObjectName("show_admin_info")
        self.toolBox = QtWidgets.QToolBox(self.tab_3)
        self.toolBox.setGeometry(QtCore.QRect(10, 90, 831, 561))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 831, 501))
        self.page.setObjectName("page")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 50, 481, 451))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 821, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(0, 20, 811, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(600, 250, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(490, 290, 321, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.page)
        self.spinBox.setGeometry(QtCore.QRect(550, 330, 261, 31))
        self.spinBox.setObjectName("spinBox")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(490, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.show_table_2 = QtWidgets.QPushButton(self.page)
        self.show_table_2.setGeometry(QtCore.QRect(490, 100, 321, 31))
        self.show_table_2.setObjectName("show_table_2")
        self.select_table_2 = QtWidgets.QComboBox(self.page)
        self.select_table_2.setGeometry(QtCore.QRect(490, 50, 321, 31))
        self.select_table_2.setEditable(False)
        self.select_table_2.setObjectName("select_table_2")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.select_table_2.addItem("")
        self.delete_values_1 = QtWidgets.QPushButton(self.page)
        self.delete_values_1.setGeometry(QtCore.QRect(490, 150, 321, 31))
        self.delete_values_1.setObjectName("delete_values_1")
        self.delete_values_3 = QtWidgets.QPushButton(self.page)
        self.delete_values_3.setGeometry(QtCore.QRect(490, 200, 321, 31))
        self.delete_values_3.setObjectName("delete_values_3")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page_2.setObjectName("page_2")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 50, 481, 441))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 821, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 811, 31))
        self.label_4.setObjectName("label_4")
        self.select_table_3 = QtWidgets.QComboBox(self.page_2)
        self.select_table_3.setGeometry(QtCore.QRect(490, 50, 321, 31))
        self.select_table_3.setObjectName("select_table_3")
        self.select_table_3.addItem("")
        self.select_table_3.addItem("")
        self.select_table_3.addItem("")
        self.select_table_3.addItem("")
        self.update_2 = QtWidgets.QPushButton(self.page_2)
        self.update_2.setGeometry(QtCore.QRect(490, 150, 321, 31))
        self.update_2.setObjectName("update_2")
        self.show_table_3 = QtWidgets.QPushButton(self.page_2)
        self.show_table_3.setGeometry(QtCore.QRect(490, 100, 321, 31))
        self.show_table_3.setObjectName("show_table_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 290, 321, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(490, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(600, 250, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_2)
        self.spinBox_2.setGeometry(QtCore.QRect(550, 330, 261, 31))
        self.spinBox_2.setObjectName("spinBox_2")
        self.delete_values_2 = QtWidgets.QPushButton(self.page_2)
        self.delete_values_2.setGeometry(QtCore.QRect(490, 200, 321, 31))
        self.delete_values_2.setObjectName("delete_values_2")
        self.toolBox.addItem(self.page_2, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.show_about = QtWidgets.QPushButton(self.widget)
        self.show_about.setGeometry(QtCore.QRect(10, 10, 831, 31))
        self.show_about.setObjectName("show_about")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 831, 611))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.widget, "")

        self.retranslateUi(project_admin)
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(project_admin)

    def retranslateUi(self, project_admin):
        _translate = QtCore.QCoreApplication.translate
        project_admin.setWindowTitle(_translate("project_admin", "Form"))
        self.folder.setText(_translate("project_admin", "Папку"))
        self.disk_media.setText(_translate("project_admin", "Носитель/Диск"))
        self.file.setText(_translate("project_admin", "Файл"))
        self.start.setText(_translate("project_admin", "Пуск"))
        self.label_2.setText(_translate("project_admin", "Сканировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("project_admin", "Анализатор"))
        self.label.setText(_translate("project_admin", "Фильтры"))
        self.sort_to_new.setItemText(0, _translate("project_admin", "Сначала новые"))
        self.sort_to_new.setItemText(1, _translate("project_admin", "Сначала старые"))
        self.fol_name.setPlaceholderText(_translate("project_admin", "По названию папки"))
        self.drop_filt.setText(_translate("project_admin", "Сбросить фильтры"))
        self.delete_all.setText(_translate("project_admin", "Удалить все записи"))
        self.sort.setText(_translate("project_admin", "Отсортировать"))
        self.work.setCurrentText(_translate("project_admin", "Сначала маленькие"))
        self.work.setItemText(0, _translate("project_admin", "Сначала маленькие"))
        self.work.setItemText(1, _translate("project_admin", "Сначала большие"))
        self.comboBox.setItemText(0, _translate("project_admin", "Показать историю сканирования папок"))
        self.comboBox.setItemText(1, _translate("project_admin", "Показать историю сканирования файлов"))
        self.comboBox.setItemText(2, _translate("project_admin", "Показать историю сканирования дисков"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("project_admin", "История запросов"))
        self.show_admin_info.setText(_translate("project_admin", "Показать информацию об администраторе"))
        self.label_7.setText(_translate("project_admin", "Выбранная таблица"))
        self.label_8.setText(_translate("project_admin", "Данная таблица о "))
        self.label_9.setText(_translate("project_admin", "Сортировка"))
        self.lineEdit.setPlaceholderText(_translate("project_admin", "Введите имя пользователя"))
        self.label_10.setText(_translate("project_admin", "По ID"))
        self.show_table_2.setText(_translate("project_admin", "Показать таблицу"))
        self.select_table_2.setPlaceholderText(_translate("project_admin", "Выбрать таблицу..."))
        self.select_table_2.setItemText(0, _translate("project_admin", "auth_group"))
        self.select_table_2.setItemText(1, _translate("project_admin", "auth_group_permissions"))
        self.select_table_2.setItemText(2, _translate("project_admin", "auth_permission"))
        self.select_table_2.setItemText(3, _translate("project_admin", "auth_user"))
        self.select_table_2.setItemText(4, _translate("project_admin", "auth_user_groups"))
        self.select_table_2.setItemText(5, _translate("project_admin", "auth_user_user_permissions"))
        self.delete_values_1.setText(_translate("project_admin", "Удалить значения таблицы"))
        self.delete_values_3.setText(_translate("project_admin", "Сбросить фильтры"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("project_admin", "auth таблицы"))
        self.label_3.setText(_translate("project_admin", "Выбранная таблица"))
        self.label_4.setText(_translate("project_admin", "Данная таблица о "))
        self.select_table_3.setPlaceholderText(_translate("project_admin", "Выбрать таблицу..."))
        self.select_table_3.setItemText(0, _translate("project_admin", "django_admin_log"))
        self.select_table_3.setItemText(1, _translate("project_admin", "django_content_type"))
        self.select_table_3.setItemText(2, _translate("project_admin", "django_migrations"))
        self.select_table_3.setItemText(3, _translate("project_admin", "django_session"))
        self.update_2.setText(_translate("project_admin", "Сбросить фильтры"))
        self.show_table_3.setText(_translate("project_admin", "Показать таблицу"))
        self.lineEdit_2.setPlaceholderText(_translate("project_admin", "Введите имя пользователя"))
        self.label_12.setText(_translate("project_admin", "По ID"))
        self.label_11.setText(_translate("project_admin", "Сортировка"))
        self.delete_values_2.setText(_translate("project_admin", "Удалить значения таблицы"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("project_admin", "django таблицы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("project_admin", "Администратор"))
        self.show_about.setText(_translate("project_admin", "Показать информацию"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("project_admin", "О проекте"))

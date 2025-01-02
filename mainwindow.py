import sys
import sqlite3
import csv
import os
from changeuser import Changeuser
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QInputDialog
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from addwidget import AddWidget
from moykalendar import Kalenar
from settings import Usersettings
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 413)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.taxch = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.taxch.setGeometry(QtCore.QRect(190, 20, 70, 17))
        self.taxch.setObjectName("taxch")
        self.incomech = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.incomech.setGeometry(QtCore.QRect(270, 20, 70, 17))
        self.incomech.setObjectName("incomech")
        self.expensech = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.expensech.setGeometry(QtCore.QRect(360, 20, 70, 17))
        self.expensech.setObjectName("expensech")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(190, 70, 521, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.csvButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.csvButton.setGeometry(QtCore.QRect(580, 340, 131, 23))
        self.csvButton.setObjectName("csvButton")
        self.sortch = QtWidgets.QComboBox(parent=self.centralwidget)
        self.sortch.setGeometry(QtCore.QRect(570, 20, 141, 22))
        self.sortch.setObjectName("sortch")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 20, 101, 16))
        self.label.setObjectName("label")
        self.changeProfile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.changeProfile.setGeometry(QtCore.QRect(30, 110, 121, 21))
        self.changeProfile.setObjectName("changeProfile")
        self.settings = QtWidgets.QPushButton(parent=self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(30, 140, 121, 23))
        self.settings.setObjectName("settings")
        self.imgelbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.imgelbl.setGeometry(QtCore.QRect(0, 0, 47, 41))
        self.imgelbl.setText("")
        self.imgelbl.setObjectName("imgelbl")
        self.surnamelbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.surnamelbl.setGeometry(QtCore.QRect(60, 0, 91, 16))
        self.surnamelbl.setText("")
        self.surnamelbl.setObjectName("surnamelbl")
        self.namelbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.namelbl.setGeometry(QtCore.QRect(60, 20, 91, 16))
        self.namelbl.setText("")
        self.namelbl.setObjectName("namelbl")
        self.patroniclbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.patroniclbl.setGeometry(QtCore.QRect(60, 40, 91, 16))
        self.patroniclbl.setText("")
        self.patroniclbl.setObjectName("patroniclbl")
        self.addSth = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addSth.setGeometry(QtCore.QRect(190, 340, 75, 23))
        self.addSth.setObjectName("addSth")
        self.openCalendar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.openCalendar.setGeometry(QtCore.QRect(30, 290, 121, 41))
        self.openCalendar.setObjectName("openCalendar")
        self.reverseRB = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.reverseRB.setGeometry(QtCore.QRect(570, 50, 111, 17))
        self.reverseRB.setObjectName("reverseRB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.taxch.setText(_translate("MainWindow", "Налоги"))
        self.incomech.setText(_translate("MainWindow", "Доходы"))
        self.expensech.setText(_translate("MainWindow", "Расходы"))
        self.csvButton.setText(_translate("MainWindow", "Импортировать в csv"))
        self.label.setText(_translate("MainWindow", "Сортировать по"))
        self.changeProfile.setText(_translate("MainWindow", "Сменить профиль"))
        self.settings.setText(_translate("MainWindow", "Настройки профиля"))
        self.addSth.setText(_translate("MainWindow", "Добавить"))
        self.openCalendar.setText(_translate("MainWindow", "Открыть календарь"))
        self.reverseRB.setText(_translate("MainWindow", "по возрастанию"))


def searh_image_by_name(folder_path, image_name):
    # Приводим имя изображения к нижнему регистру для сравнения
    image_name_lower = image_name.lower()

    # Проходим по всем файлам в указанной папке
    for filename in os.listdir(folder_path):
        # Получаем имя файла без расширения
        name, ex = os.path.splitext(filename)

        # Проверяем, совпадает ли имя файла с искомым (без учета регистра)
        if name.lower() == image_name_lower:
            return name + ex
    return ''


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, is_enter, data):
        super().__init__()
        self.setupUi(self)
        if is_enter:
            self.con = sqlite3.connect('taxbook.db')
            self.cur = self.con.cursor()
            m = self.cur.execute("""SELECT Lastname, Firstname, Patronymic, UserID FROM Users""").fetchall()
            a = QInputDialog.getItem(self, 'Вход', 'Выберите пользователя',
                                     [' '.join([str(j) for j in i]) for i in m], 0, False)[0]
            pw, ok = QInputDialog.getText(self, 'Введите пароль', 'Пароль')
            if ok:
                self.ids = a.split()[-1]
                if pw == self.cur.execute("""SELECT Password FROM Users WHERE UserID=?""", (self.ids,
                                                                                            )).fetchall()[0][
                    0]:
                    self.surnamelbl.setText(a.split()[0])
                    self.namelbl.setText(a.split()[1])
                    self.patroniclbl.setText(a.split()[2])
                else:
                    QMessageBox.warning(self, 'Ошибка', 'Неправильный пароль')
                    sys.exit()
            else:
                sys.exit()
        else:
            self.con = sqlite3.connect('taxbook.db')
            self.cur = self.con.cursor()
            self.cur.execute(
                """INSERT INTO Users (Userid, Lastname, Firstname, Patronymic, TypeOfWork, password) 
                VALUES (COALESCE((SELECT MAX(Userid) FROM Users), 0) + 1, ?, ?, ?, ?, ?)""",
                (data[0], data[1], data[2], data[3], data[4])
            )
            self.con.commit()  # Не забудем зафиксировать изменения
            self.surnamelbl.setText(data[0])
            self.namelbl.setText(data[1])
            self.patroniclbl.setText(data[2])
            self.ids = self.cur.execute("""SELECT MAX(Userid) FROM Users""").fetchone()[0]
        self.imgelbl.setText('Нет фото')
        self.qpix = QPixmap(f'images\\{self.ids}.png')
        self.imgelbl.setPixmap(self.qpix)
        self.imgelbl.setScaledContents(True)

        self.setWindowIcon(QIcon("icon.png"))
        self.qp = None
        self.imagelbl = self.imgelbl
        self.setWindowTitle('Налоговая книжка')
        self.con = sqlite3.connect('taxbook.db')
        self.cur = self.con.cursor()
        self.addSth.clicked.connect(self.add)
        self.csvButton.clicked.connect(self.csvimport)
        self.openCalendar.clicked.connect(self.calendaropen)
        self.settings.clicked.connect(self.opensettings)
        self.changeProfile.clicked.connect(self.changeuser)
        self.taxch.setChecked(True)
        self.incomech.setChecked(True)
        self.expensech.setChecked(True)
        self.sortch.addItem('дате')
        self.sortch.addItem('сумме')
        self.incomech.clicked.connect(self.update)
        self.expensech.clicked.connect(self.update)
        self.expensech.setText('Трата')
        self.taxch.clicked.connect(self.update)
        self.sortch.currentTextChanged.connect(self.update)
        self.reverseRB.clicked.connect(self.update)
        self.reverseRB.setChecked(True)
        self.update()

    def update(self):
        if self.qp is not None:
            self.imagelbl.setPixmap(self.qp)
        a = self.cur.execute("""SELECT Lastname, Firstname, Patronymic FROM Users WHERE Userid=?""",
                             (self.ids,)).fetchall()
        self.surnamelbl.setText(a[0][0])
        self.namelbl.setText(a[0][1])
        self.patroniclbl.setText(a[0][2])
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Вид траты/дохода', 'Сумма', 'Тип', 'Дата', 'Дата уплаты'])
        self.everything = []
        if self.taxch.isChecked():
            t = self.cur.execute(
                """SELECT Sum, TaxTypes.name, date, date2 FROM Taxes INNER JOIN TaxTypes ON TaxTypes.TaxType=Taxes.TaxType WHERE Userid=?""",
                (self.ids,)).fetchall()
            for row in t:
                row = ['Налог'] + list(row)[:]
                self.everything.append(row)
        if self.expensech.isChecked():
            v = self.cur.execute(
                """SELECT Sum, name, date FROM Expenses INNER JOIN ExpenseTypes ON ExpenseType=Category WHERE Userid=?""",
                (self.ids,)).fetchall()
            for row in v:
                row = ['Трата'] + list(row)[:]
                self.everything.append(row)
        if self.incomech.isChecked():
            b = self.cur.execute(
                """SELECT Sum, IncomeTypes.name, date FROM Incomes INNER JOIN IncomeTypes ON IncomeTypes.IncomeType=Incomes.IncomeType WHERE Userid=?""",
                (
                    self.ids,)).fetchall()
            for row in b:
                row = ['Доход'] + list(row)[:]
                self.everything.append(row)
        if self.sortch.currentText() == 'дате':
            self.everything = sorted(self.everything, key=lambda x: (
                int(x[3].split('.')[2]), int(x[3].split('.')[1]), int(x[3].split('.')[0])),
                                     reverse=self.reverseRB.isChecked()
                                     )
        elif self.sortch.currentText() == 'сумме':
            self.everything = sorted(self.everything, key=lambda x: int(x[1]), reverse=self.reverseRB.isChecked())

            # Обновление таблицы
        print(self.everything)
        self.tableWidget.setRowCount(0)  # Сначала очищаем таблицу
        for i, row in enumerate(self.everything):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, el in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(el)))

    def changeuser(self):
        form = Changeuser(self)
        form.show()

    def opensettings(self):
        form = Usersettings(self)
        form.show()

    # открывает календарь
    def calendaropen(self):
        form = Kalenar(self)
        form.show()

    def csvimport(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "CSV Files (*.csv);;All Files (*)",
                                                   )
        if file_name:
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in range(self.tableWidget.rowCount()):
                    row_data = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        row_data.append(item.text() if item else "")
                    writer.writerow(row_data)

    def add(self):
        form = AddWidget(self)
        form.show()

    def closeEvent(self, event):
        self.con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

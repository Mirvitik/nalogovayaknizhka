from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QDate
import sqlite3
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 318)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar1 = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendar1.setGeometry(QtCore.QRect(10, 10, 312, 183))
        self.calendar1.setObjectName("calendar1")
        self.calendar2 = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendar2.setGeometry(QtCore.QRect(330, 10, 312, 183))
        self.calendar2.setObjectName("calendar2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 210, 47, 13))
        self.label.setObjectName("label")
        self.tax_progress = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.tax_progress.setGeometry(QtCore.QRect(60, 210, 161, 23))
        self.tax_progress.setProperty("value", 24)
        self.tax_progress.setObjectName("tax_progress")
        self.income_progress = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.income_progress.setGeometry(QtCore.QRect(270, 210, 131, 23))
        self.income_progress.setProperty("value", 24)
        self.income_progress.setObjectName("income_progress")
        self.expense_progress = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.expense_progress.setGeometry(QtCore.QRect(480, 210, 131, 23))
        self.expense_progress.setProperty("value", 24)
        self.expense_progress.setObjectName("expense_progress")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 210, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 210, 47, 13))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
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
        self.label.setText(_translate("MainWindow", "Налоги:"))
        self.label_2.setText(_translate("MainWindow", "Доходы:"))
        self.label_3.setText(_translate("MainWindow", "Траты:"))


def count_rows_in_date_range(start_date, end_date, tip):
    con = sqlite3.connect('taxbook.db')
    cur = con.cursor()
    qur = """SELECT date FROM {}""".format(tip)
    taxm = cur.execute(qur).fetchall()
    cnttax = 0
    print(start_date, end_date, taxm)
    for el in taxm:
        if (int(start_date.split('.')[0]), int(start_date.split('.')[1]), int(start_date.split('.')[2])) <= (
                int(el[0].split('.')[2]), int(el[0].split('.')[1]), int(el[0].split('.')[0])) <= (
                int(end_date.split('.')[0]), int(end_date.split('.')[1]), int(end_date.split('.')[2])):
            cnttax += 1
    print(cnttax)
    percentage = (cnttax / len(taxm) * 100) if len(taxm) > 0 else 0
    return percentage


# Пример использования

class Kalenar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.d = ''
        self.d2 = ''
        self.setWindowTitle("Выберите промежуток дат")
        self.setGeometry(100, 100, 650, 300)  # Увеличиваем ширину окна
        # Создаем первый виджет календаря
        self.calendar1.setGridVisible(True)
        self.calendar1.clicked.connect(self.date_selected)

        # Создаем второй виджет календаря
        self.calendar2.setGridVisible(True)
        self.calendar2.clicked.connect(self.update_left_calendar_limit)

        # Добавляем горизонтальный макет с календарями в основной макет

        # Создаем ProgressBar для Налогов

        self.tax_progress.setValue(0)  # Пример значения

        # Создаем ProgressBar для Доходов
        self.income_progress.setValue(0)  # Пример значения

        # Создаем ProgressBar для Трат
        self.expense_progress.setValue(0)  # Пример значения

        # Добавляем макет ProgressBar в основной макет

    def date_selected(self, date: QDate):
        # Получаем день, месяц и год
        day = date.day()
        month = date.month()  # Месяц в виде числа
        year = date.year()
        self.d = '.'.join(map(str, [year, month, day]))
        taxes = self.parent().cur.execute("""SELECT date FROM Taxes WHERE UserID=?""", (self.parent().ids,)).fetchall()
        taxes_new = []
        for el in taxes:
            el = el[0].split('.')
            if el[0] == date.day() and el[1] == date.month() and el[2] == date.year():
                taxes_new.append(el)

        # Выводим выбранную дату в консоль в формате "день.месяц.год"
        try:
            self.tax_progress.setValue(round(count_rows_in_date_range(self.d, self.d2, 'Taxes')))
            self.income_progress.setValue(round(count_rows_in_date_range(self.d, self.d2, 'Incomes')))
            self.expense_progress.setValue(round(count_rows_in_date_range(self.d, self.d2, 'Expenses')))
            self.statusbar.showMessage('')
        except Exception:
            self.statusbar.showMessage('Выберите дату справа, а затем дату слева')

    def update_left_calendar_limit(self):
        # Получаем выбранную дату на правом календаре
        right_date = self.calendar2.selectedDate()
        self.d2 = '.'.join(map(str, [right_date.year(), right_date.month(), right_date.day()]))
        # Устанавливаем максимальную дату на левом календаре
        self.calendar1.setMaximumDate(right_date)

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 275)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.typem = QtWidgets.QComboBox(parent=self.centralwidget)
        self.typem.setGeometry(QtCore.QRect(170, 10, 281, 22))
        self.typem.setObjectName("typem")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.summa = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.summa.setGeometry(QtCore.QRect(170, 40, 281, 22))
        self.summa.setObjectName("summa")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.type = QtWidgets.QComboBox(parent=self.centralwidget)
        self.type.setGeometry(QtCore.QRect(170, 70, 281, 22))
        self.type.setObjectName("type")
        self.date = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.date.setGeometry(QtCore.QRect(170, 100, 281, 22))
        self.date.setObjectName("date")
        self.date2 = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.date2.setGeometry(QtCore.QRect(170, 130, 281, 22))
        self.date2.setObjectName("date2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 111, 16))
        self.label_5.setObjectName("label_5")
        self.cancelbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(280, 200, 75, 23))
        self.cancelbtn.setObjectName("cancelbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
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
        self.label.setText(_translate("MainWindow", "Тип траты/дохода"))
        self.label_2.setText(_translate("MainWindow", "Сумма"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label_3.setText(_translate("MainWindow", "Тип"))
        self.label_4.setText(_translate("MainWindow", "Дата получения"))
        self.label_5.setText(_translate("MainWindow", "Дата уплаты"))
        self.cancelbtn.setText(_translate("MainWindow", "Отмена"))


# функция добавления ведущих нулей
def vednul(s):
    s = str(s)
    if len(s) < 2:
        return '0' + s
    return s


class AddWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Добавить')
        self.typem.addItems(['Налог', 'Трата', 'Доход'])
        self.typem.currentTextChanged.connect(self.hideit)
        self.pushButton.clicked.connect(self.save)
        self.cancelbtn.clicked.connect(self.cancel)
        self.summa.setMaximum(2_147_483_647)
        self.cur = self.parent().cur
        self.hideit()

    def save(self):
        # что добавляем в базу
        match self.typem.currentText():
            case 'Налог':  # налог-2 даты
                a = self.cur.execute("""SELECT TaxType FROM TaxTypes WHERE name=?""",
                                     (self.type.currentText(),)).fetchone()
                if a is None:
                    a = (0,)
                if (int(self.date.date().year()), int(self.date.date().month()), int(self.date.date().day())) <= (
                        int(self.date2.date().year()), int(self.date2.date().month()), int(self.date2.date().day())):
                    self.cur.execute(
                        """INSERT INTO Taxes(Userid, Sum, TaxType, Date, Date2) VALUES(?, ?, ?, ?, ?)""", (
                            self.parent().ids, self.summa.value(), a[0],
                            '.'.join(
                                [vednul(self.date.date().day()), vednul(self.date.date().month()),
                                 str(self.date.date().year())]),
                            '.'.join([vednul(self.date2.date().day()), vednul(self.date2.date().month()),
                                      str(self.date2.date().year())])))
                else:
                    QMessageBox.warning(self, 'Ошибка', 'Ошибка, дата получения налога больше даты уплаты')
            case 'Доход':
                a = self.cur.execute(
                    """SELECT IncomeType FROM IncomeTypes WHERE name=?""", (self.type.currentText(),)).fetchone()
                if a is None:
                    a = (0,)
                self.cur.execute("""INSERT INTO Incomes(Userid, Sum, IncomeType, Date) VALUES(?, ?, ?, ?)""", (
                    self.parent().ids, self.summa.value(), a[0],
                    '.'.join(
                        [vednul(self.date.date().day()), vednul(self.date.date().month()),
                         str(self.date.date().year())])))
            case 'Трата':
                a = self.cur.execute("""SELECT ExpenseType FROM ExpenseTypes WHERE name=?""",
                                     (self.type.currentText(),)).fetchone()
                if a is None:
                    a = (0,)
                self.cur.execute("""INSERT INTO Expenses(Userid, Sum, Category, Date) VALUES(?, ?, ?, ?)""", (
                    self.parent().ids, self.summa.value(), a[0],
                    '.'.join(
                        [vednul(self.date.date().day()), vednul(self.date.date().month()),
                         str(self.date.date().year())])))
        self.parent().con.commit()
        self.parent().update()
        self.close()

    def cancel(self):
        self.close()

    def hideit(self):
        self.type.clear()
        if self.typem.currentText() != 'Налог':
            self.date2.hide()
            self.label_5.hide()
            if self.typem.currentText() == 'Доход':
                data = self.cur.execute("""SELECT name FROM IncomeTypes""").fetchall()
                self.type.addItems([str(i[0]) for i in data])
            else:
                data = self.cur.execute("""SELECT name FROM ExpenseTypes""").fetchall()
                self.type.addItems([str(i[0]) for i in data])
        else:
            self.date2.show()
            self.label_5.show()
            data = self.cur.execute("""SELECT name FROM TaxTypes""").fetchall()
            self.type.addItems([str(i[0]) for i in data])

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QInputDialog, QFormLayout, QDialog, QLineEdit, QPushButton, \
    QMessageBox
import sqlite3
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 167)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 30, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 20))
        self.label.setObjectName("label")
        self.enterbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.enterbtn.setGeometry(QtCore.QRect(230, 90, 75, 23))
        self.enterbtn.setObjectName("enterbtn")
        self.createbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createbtn.setGeometry(QtCore.QRect(30, 90, 101, 23))
        self.createbtn.setObjectName("createbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 21))
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
        self.label.setText(_translate("MainWindow", "Выбери пользователя"))
        self.enterbtn.setText(_translate("MainWindow", "Войти"))
        self.createbtn.setText(_translate("MainWindow", "Создать новго"))



class RegDialog(QDialog):
    def __init__(self):
        # инийиализируем виджеты форму для ввода данных
        super().__init__()
        self.setWindowTitle("Зарегистрируйтесь")

        self.layout = QFormLayout(self)

        self.s_input = QLineEdit(self)
        self.name_input = QLineEdit(self)
        self.p_input = QLineEdit(self)
        self.job_type_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.repeat_password_input = QLineEdit(self)
        self.repeat_password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.layout.addRow("Фамилия:", self.s_input)
        self.layout.addRow("Имя:", self.name_input)
        self.layout.addRow("Отчество:", self.p_input)
        self.layout.addRow("Тип работы:", self.job_type_input)
        self.layout.addRow("Пароль:", self.password_input)
        self.layout.addRow("Повторите пароль:", self.repeat_password_input)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.clicked.connect(self.on_submit)
        self.layout.addWidget(self.submit_button)

    def on_submit(self):
        # проверка данных
        if not bool(self.s_input.text()):
            QMessageBox.warning(self, "Ошибка", "Введите фамилию!")
            return
        if not bool(self.name_input.text()):
            QMessageBox.warning(self, "Ошибка", "Введите имя!")
            return
        # Проверка паролей
        if self.password_input.text() != self.repeat_password_input.text():
            QMessageBox.warning(self, "Ошибка", "Пароли не совпадают!")
            return False
        if self.password_input.text().lower() == self.password_input.text():
            QMessageBox.warning(self, "Ошибка", "Добавьте заглавные буквы в пароль!")
            return False
        if self.password_input.text().upper() == self.password_input.text():
            QMessageBox.warning(self, "Ошибка", "Добавьте строчные буквы в пароль!")
            return False
        if self.password_input.text().isalpha():
            QMessageBox.warning(self, "Ошибка", "Добавьте цифры буквы в пароль!")
            return False
        if len(self.password_input.text()) < 8:
            QMessageBox.warning(self, "Ошибка", "Длина пароля должна быть не менее 8!")
            return False
        self.close()
        return True


class Changeuser(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Вход/регистрация')
        self.con = sqlite3.connect('taxbook.db')
        self.cur = self.con.cursor()
        m = self.cur.execute("""SELECT Lastname, Firstname, Patronymic, UserID FROM Users""").fetchall()
        self.comboBox.addItems([' '.join([str(j) for j in i]) for i in m])
        self.comboBox.setEditable(False)
        self.enterbtn.clicked.connect(self.run)
        self.createbtn.clicked.connect(self.createuser)

    def run(self):
        pw, ok = QInputDialog.getText(self, 'Введите пароль', 'Пароль')
        print(pw, ok)
        print(self.cur.execute("""SELECT password FROM Users WHERE UserID=?""",
                               (self.comboBox.currentText().split()[-1])).fetchall()[0][0])
        if ok and pw == self.cur.execute("""SELECT password FROM Users WHERE UserID=?""",
                                         (self.comboBox.currentText().split()[-1])).fetchall()[0][0]:
            self.parent().surnamelbl.setText(self.comboBox.currentText().split()[0])
            self.parent().namelbl.setText(self.comboBox.currentText().split()[1])
            self.parent().patroniclbl.setText(self.comboBox.currentText().split()[2])
            self.parent().ids = self.comboBox.currentText().split()[-1]
            self.parent().imagelbl.setPixmap(QPixmap(f'images/{self.parent().ids}.png'))
            self.parent().update()
            self.close()
        elif pw != self.cur.execute("""SELECT password FROM Users WHERE UserID=?""",
                                    (self.comboBox.currentText().split()[-1])).fetchall()[0][0]:
            QMessageBox.warning(self, 'Ошибка', 'Пароли не совпадают')

    def createuser(self):
        dialog = RegDialog()
        dialog.exec()
        if dialog.on_submit():
            # Если данные введены корректно, открываем главное окно
            data = [dialog.s_input.text(), dialog.name_input.text(), dialog.p_input.text(),
                    dialog.job_type_input.text(),
                    dialog.password_input.text()]
            self.cur.execute(
                """INSERT INTO Users (Userid, Lastname, Firstname, Patronymic, TypeOfWork, password) 
                VALUES (COALESCE((SELECT MAX(Userid) FROM Users), 0) + 1, ?, ?, ?, ?, ?)""",
                (data[0], data[1], data[2], data[3], data[4])
            )
            self.con.commit()  # Не забудьте зафиксировать изменения
            self.parent().surnamelbl.setText(data[0])
            self.parent().namelbl.setText(data[1])
            self.parent().patroniclbl.setText(data[2])
            self.parent().ids = self.cur.execute("""SELECT MAX(Userid) FROM Users""").fetchone()[0]
            self.parent().update()
            self.con.close()
            self.close()

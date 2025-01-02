from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QInputDialog
import shutil
import os
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 267)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Lastname = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Lastname.setGeometry(QtCore.QRect(260, 20, 113, 20))
        self.Lastname.setObjectName("Lastname")
        self.Firstname = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Firstname.setGeometry(QtCore.QRect(260, 50, 113, 20))
        self.Firstname.setObjectName("Firstname")
        self.Patronymic = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Patronymic.setGeometry(QtCore.QRect(260, 80, 113, 20))
        self.Patronymic.setObjectName("Patronymic")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 50, 47, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 80, 81, 16))
        self.label_3.setObjectName("label_3")
        self.image = QtWidgets.QLabel(parent=self.centralwidget)
        self.image.setGeometry(QtCore.QRect(10, 30, 81, 81))
        self.image.setObjectName("image")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label_5.setObjectName("label_5")
        self.addphoto = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addphoto.setGeometry(QtCore.QRect(10, 130, 101, 23))
        self.addphoto.setObjectName("addphoto")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(220, 190, 156, 23))
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.deletebtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deletebtn.setGeometry(QtCore.QRect(10, 160, 121, 23))
        self.deletebtn.setObjectName("deletebtn")
        self.jobtype = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.jobtype.setGeometry(QtCore.QRect(260, 110, 113, 20))
        self.jobtype.setObjectName("jobtype")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 110, 71, 16))
        self.label_4.setObjectName("label_4")
        self.changePass = QtWidgets.QPushButton(parent=self.centralwidget)
        self.changePass.setGeometry(QtCore.QRect(10, 190, 121, 23))
        self.changePass.setObjectName("changePass")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
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
        self.label.setText(_translate("MainWindow", "Фамлия"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.label_3.setText(_translate("MainWindow", "Отчество"))
        self.image.setText(_translate("MainWindow", "У вас нет фото"))
        self.label_5.setText(_translate("MainWindow", "Фотография"))
        self.addphoto.setText(_translate("MainWindow", "Добавить фото"))
        self.deletebtn.setText(_translate("MainWindow", "Удалить профиль"))
        self.label_4.setText(_translate("MainWindow", "Тип работы"))
        self.changePass.setText(_translate("MainWindow", "Сменить пароль"))


def delete_image_by_name(folder_path, image_name):
    # Приводим имя изображения к нижнему регистру для сравнения
    image_name_lower = image_name.lower()

    # Флаг для отслеживания, найдено ли изображение

    # Проходим по всем файлам в указанной папке
    for filename in os.listdir(folder_path):
        # Получаем имя файла без расширения
        name, _ = os.path.splitext(filename)
        print(_)

        # Проверяем, совпадает ли имя файла с искомым (без учета регистра)
        if name.lower() == image_name_lower:
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path)  # Удаляем файл
                print(f'Удален файл: {file_path}')
            except Exception as e:
                print(f'Ошибка при удалении файла {file_path}: {e}')


class Usersettings(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Настройки')
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.close)
        self.deletebtn.clicked.connect(self.delete)
        self.addphoto.clicked.connect(self.photo)
        self.Lastname.setText(self.parent().surnamelbl.text())
        self.Firstname.setText(self.parent().namelbl.text())
        self.Patronymic.setText(self.parent().patroniclbl.text())
        self.changePass.clicked.connect(self.changep)
        self.jobtype.setText(
            self.parent().cur.execute("""SELECT TypeOfWork FROM Users WHERE UserID=?""",
                                      (self.parent().ids,)).fetchone()[0])
        self.con = self.parent().con
        self.cur = self.parent().cur
        self.image.setText('Нет фото')
        self.image.setScaledContents(True)
        qp = QPixmap(f'images/{self.parent().ids}.png')
        self.image.setPixmap(qp)

    def accept(self):
        if all([bool(i) for i in (self.Lastname.text(), self.Firstname.text())]):
            self.cur.execute("""UPDATE Users
                                SET Lastname=?, Firstname=?, Patronymic=?, TypeOfWork=?
                                WHERE Userid=?""",
                             (self.Lastname.text(), self.Firstname.text(), self.Patronymic.text(), self.jobtype.text(),
                              self.parent().ids))
            self.con.commit()
            self.parent().update()
            self.close()
        else:
            self.statusbar.showMessage('Неправильный ввод')

    def delete(self):
        q = QMessageBox.question(self, 'Удаление', 'Удалить профиль?',
                                 buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if q == QMessageBox.StandardButton.Yes:
            self.cur.execute("""DELETE FROM Users
                                WHERE Userid=?""", (self.parent().ids,))
            self.cur.execute("""DELETE FROM Taxes
                                WHERE Userid=?""", (self.parent().ids,))
            self.cur.execute("""DELETE FROM Expenses
                                        WHERE Userid=?""", (self.parent().ids,))
            self.cur.execute("""DELETE FROM Incomes
                                        WHERE Userid=?""", (self.parent().ids,))
            image_path = os.path.join('images', f'{self.parent().ids}.png')
            try:
                # Проверяем, существует ли файл
                if os.path.isfile(image_path):
                    os.remove(image_path)  # Удаляем файл
            except Exception:
                pass
            self.parent().con.commit()
            self.parent().close()
            self.close()

    def photo(self):
        QMessageBox.warning(self, 'Внимание', 'Во избежание ошибок загружайте только .png фотографии')
        fname, ok = QFileDialog.getOpenFileName(self, '', '')
        if ok and fname != '':
            delete_image_by_name('images', str(self.parent().ids))
            qp = QPixmap(fname)
            self.parent().qp = qp
            self.parent().imagelbl.setScaledContents(True)
            self.image.setScaledContents(True)
            self.image.setPixmap(qp)
            image_path = fname
            new_name = str(self.parent().ids)
            # Проверяем, существует ли файл
            if not os.path.isfile(image_path):
                print("Ошибка: Файл не найден по указанному пути.")
                return

            # Получаем директорию файла
            directory = os.path.dirname(image_path)

            # Создаем папку images, если она не существует
            images_folder = os.path.join(directory, 'images')
            os.makedirs(images_folder, exist_ok=True)

            # Получаем расширение файла
            file_extension = os.path.splitext(image_path)[1]

            # Создаем новый путь для перемещения
            new_image_path = os.path.join(os.getcwd() + '\\images', f"{new_name}{file_extension}")

            # Проверяем, существует ли файл с таким же именем

            # Переименовываем и перемещаем файл
            try:
                shutil.move(image_path, new_image_path)
                print(f"Файл переименован и перемещен в: {new_image_path}")
            except Exception as e:
                print(f"Ошибка при перемещении файла: {e}")

    def changep(self):
        old = self.cur.execute("""SELECT password FROM Users WHERE Userid=?""", (self.parent().ids,)).fetchall()[0][0]
        p, ok = QInputDialog.getText(self, 'Введите пароль', 'Пароль')
        if ok:
            if p == old:
                newp, nok = QInputDialog.getText(self, 'Введите пароль', 'Пароль')
                if nok:
                    if newp.lower() == newp:
                        QMessageBox.warning(self, "Ошибка", "Добавьте заглавные буквы в пароль!")
                        return
                    if newp.upper() == newp:
                        QMessageBox.warning(self, "Ошибка", "Добавьте строчные буквы в пароль!")
                        return
                    if newp.isalpha():
                        QMessageBox.warning(self, "Ошибка", "Добавьте цифры буквы в пароль!")
                        return
                    if len(newp) < 8:
                        QMessageBox.warning(self, "Ошибка", "Длина пароля должна быть не менее 8!")
                        return
                    self.cur.execute("""UPDATE Users
                                        SET password=?
                                        WHERE Userid=?""", (newp, self.parent().ids))
            else:
                QMessageBox.warning(self, 'Ошибка', 'Пароли не совподают')

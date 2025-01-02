from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox


class RegDialog(QDialog):
    def __init__(self):
        # инициализируем виджеты форму для ввода данных
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

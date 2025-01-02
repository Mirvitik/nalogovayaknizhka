import sqlite3
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

from mainwindow import MainWindow
from registration import RegDialog


# функция для вывода ошибок
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


con = sqlite3.connect('taxbook.db')
# проверяем открыто ли приложение впервые
# если впервые просим зарегистрироваться, иначе-войти
app = QApplication(sys.argv)
app.setWindowIcon(QIcon('icon.png'))
cur = con.cursor()
if len(cur.execute("""SELECT * FROM Users""").fetchall()) == 0:
    # Создаем и показываем диалоговое окно
    dialog = RegDialog()
    dialog.exec()
    if dialog.on_submit():
        # Если данные введены корректно, открываем главное окно
        data = [dialog.s_input.text(), dialog.name_input.text(), dialog.p_input.text(), dialog.job_type_input.text(),
                dialog.password_input.text()]
        main_window = MainWindow(is_enter=False, data=data)
        main_window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
else:
    form = MainWindow(is_enter=True, data=[])
    form.show()
    sys.excepthook = except_hook
sys.excepthook = except_hook
sys.exit(app.exec())

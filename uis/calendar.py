# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 318)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 21))
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
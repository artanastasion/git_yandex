from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Coffee(object):
    def setupUi(self, Coffee):
        Coffee.setObjectName("Coffee")
        Coffee.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Coffee)
        self.centralwidget.setObjectName("centralwidget")
        self.view = QtWidgets.QTableView(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(10, 20, 781, 321))
        self.view.setObjectName("view")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(20, 360, 108, 36))
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(150, 360, 108, 36))
        self.editButton.setObjectName("editButton")
        Coffee.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Coffee)
        self.statusbar.setObjectName("statusbar")
        Coffee.setStatusBar(self.statusbar)

        self.retranslateUi(Coffee)
        QtCore.QMetaObject.connectSlotsByName(Coffee)

    def retranslateUi(self, Coffee):
        _translate = QtCore.QCoreApplication.translate
        Coffee.setWindowTitle(_translate("Coffee", "MainWindow"))
        self.addButton.setText(_translate("Coffee", "Добавить"))
        self.editButton.setText(_translate("Coffee", "Изменить"))

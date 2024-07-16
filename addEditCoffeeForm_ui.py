from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEditCoffeeDialog(object):
    def setupUi(self, AddEditCoffeeDialog):
        AddEditCoffeeDialog.setObjectName("AddEditCoffeeDialog")
        AddEditCoffeeDialog.resize(539, 430)
        self.nameEdit = QtWidgets.QLineEdit(AddEditCoffeeDialog)
        self.nameEdit.setGeometry(QtCore.QRect(110, 20, 351, 36))
        self.nameEdit.setText("")
        self.nameEdit.setObjectName("nameEdit")
        self.roastEdit = QtWidgets.QLineEdit(AddEditCoffeeDialog)
        self.roastEdit.setGeometry(QtCore.QRect(110, 70, 351, 36))
        self.roastEdit.setObjectName("roastEdit")
        self.groundEdit = QtWidgets.QLineEdit(AddEditCoffeeDialog)
        self.groundEdit.setGeometry(QtCore.QRect(110, 120, 351, 36))
        self.groundEdit.setObjectName("groundEdit")
        self.descriptionEdit = QtWidgets.QLineEdit(AddEditCoffeeDialog)
        self.descriptionEdit.setGeometry(QtCore.QRect(110, 170, 351, 36))
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.priceEdit = QtWidgets.QLineEdit(AddEditCoffeeDialog)
        self.priceEdit.setGeometry(QtCore.QRect(110, 220, 351, 36))
        self.priceEdit.setObjectName("priceEdit")
        self.volumeEdit = QtWidgets.QLineEdit(AddEditCoffeeDialog)
        self.volumeEdit.setGeometry(QtCore.QRect(110, 280, 351, 36))
        self.volumeEdit.setObjectName("volumeEdit")
        self.saveButton = QtWidgets.QPushButton(AddEditCoffeeDialog)
        self.saveButton.setGeometry(QtCore.QRect(110, 340, 108, 36))
        self.saveButton.setObjectName("saveButton")
        self.cancelButton = QtWidgets.QPushButton(AddEditCoffeeDialog)
        self.cancelButton.setGeometry(QtCore.QRect(340, 340, 108, 36))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(AddEditCoffeeDialog)
        QtCore.QMetaObject.connectSlotsByName(AddEditCoffeeDialog)

    def retranslateUi(self, AddEditCoffeeDialog):
        _translate = QtCore.QCoreApplication.translate
        AddEditCoffeeDialog.setWindowTitle(_translate("AddEditCoffeeDialog", "Dialog"))
        self.nameEdit.setPlaceholderText(_translate("AddEditCoffeeDialog", "название_сорта"))
        self.roastEdit.setPlaceholderText(_translate("AddEditCoffeeDialog", "степень_обжарки"))
        self.groundEdit.setPlaceholderText(_translate("AddEditCoffeeDialog", "молотый_или_в_зернах"))
        self.descriptionEdit.setPlaceholderText(_translate("AddEditCoffeeDialog", "описание_вкуса"))
        self.priceEdit.setPlaceholderText(_translate("AddEditCoffeeDialog", "цена"))
        self.volumeEdit.setPlaceholderText(_translate("AddEditCoffeeDialog", "объем_упаковки"))
        self.saveButton.setText(_translate("AddEditCoffeeDialog", "Сохранить"))
        self.cancelButton.setText(_translate("AddEditCoffeeDialog", "Отменить"))

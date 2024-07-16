import sys
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5 import uic


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        self.model = QSqlTableModel(self, db)
        self.model.setTable('coffee')
        self.model.select()

        self.view.setModel(self.model)
        self.view.resize(1000, 1000)
        self.view.resizeColumnsToContents()
        self.setGeometry(1000, 550, 1000, 550)
        self.setWindowTitle('Кофе')

        self.addButton.clicked.connect(self.addRecord)
        self.editButton.clicked.connect(self.editRecord)

    def addRecord(self):
        dialog = AddEditCoffeeDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.model.select()
            self.view.reset()

    def editRecord(self):
        selected = self.view.selectionModel().selectedRows()
        if selected:
            row = selected[0].row()
            record = self.model.record(row)
            dialog = AddEditCoffeeDialog(self, record)
            if dialog.exec_() == QDialog.Accepted:
                self.model.select()
                self.view.reset()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Выберите запись для редактирования')


class AddEditCoffeeDialog(QDialog):
    def __init__(self, parent=None, record=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.record = record
        if self.record:
            self.loadRecordData()

        self.saveButton.clicked.connect(self.saveRecord)
        self.cancelButton.clicked.connect(self.reject)

    def loadRecordData(self):
        self.nameEdit.setText(self.record.text('название_сорта'))
        self.roastEdit.setText(self.record.text('степень_обжарки'))
        self.groundEdit.setText(self.record.text('молотый_или_в_зернах'))
        self.descriptionEdit.setText(self.record.text('описание_вкуса'))
        self.priceEdit.setText(self.record.text('цена'))
        self.volumeEdit.setText(self.record.text('объем_упаковки'))

    def saveRecord(self):
        name = self.nameEdit.text()
        roast = self.roastEdit.text()
        ground = self.groundEdit.text()
        description = self.descriptionEdit.text()
        price = self.priceEdit.text()
        volume = self.volumeEdit.text()

        if not all([name, roast, ground, description, price, volume]):
            QMessageBox.warning(self, 'Ошибка', 'Все поля должны быть заполнены')
            return

        if self.record:
            self.record.setText('название_сорта', name)
            self.record.setText('степень_обжарки', roast)
            self.record.setText('молотый_или_в_зернах', ground)
            self.record.setText('описание_вкуса', description)
            self.record.setText('цена', price)
            self.record.setText('объем_упаковки', volume)
            self.parent().model.setRecord(self.parent().view.currentIndex().row(), self.record)
        else:
            row = self.parent().model.rowCount()
            self.parent().model.insertRow(row)
            self.parent().model.setData(self.parent().model.index(row, 1), name)
            self.parent().model.setData(self.parent().model.index(row, 2), roast)
            self.parent().model.setData(self.parent().model.index(row, 3), ground)
            self.parent().model.setData(self.parent().model.index(row, 4), description)
            self.parent().model.setData(self.parent().model.index(row, 5), price)
            self.parent().model.setData(self.parent().model.index(row, 6), volume)

        if not self.parent().model.submitAll():
            QMessageBox.warning(self, 'Ошибка', 'Не удалось сохранить данные в базу данных')
            return

        self.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())

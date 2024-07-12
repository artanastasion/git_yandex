import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Cofee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()

        self.view.setModel(model)
        self.view.resize(1000, 1000)
        self.view.resizeColumnsToContents()
        self.setGeometry(1000, 550, 1000, 550)
        self.setWindowTitle('Кофе')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cofee()
    ex.show()
    sys.exit(app.exec())

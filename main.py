import sys

from PyQt6 import *

from PyQt6.QtWidgets import *
from controller import *
from login import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('easy-cheese.ui', self)

        # self.initializeLogIn()
        self.initializeCheckoutWindow()
        self.initializeInventory()
        self.initializeCustomers()
        self.initializeManager()

        self.initializeInvoicesTable()
        self.initializeActiveCustomersTable()

    def initializeCheckoutWindow(self):
        self.coProdNameCbo = self.findChild(QComboBox, 'coProdNameCbo')
        self.coQtyBO = self.findChild(QSpinBox, 'coQtyBO')
        self.coAddBtn = self.findChild(QPushButton, 'coAddBtn')
        self.coUpBtn = self.findChild(QPushButton, 'coUpBtn')
        self.coDownBtn = self.findChild(QPushButton, 'coDownBtn')
        self.coDeleteBtn = self.findChild(QPushButton, 'coDeleteBtn')
        self.coCOnfirmBtn = self.findChild(QPushButton, 'coCOnfirmBtn')
        self.coTbl = self.findChild(QTableWidget, 'coTbl')

    def initializeInventory(self):
        # Edit Product
        self.invPnameCbo = self.findChild(QComboBox, 'invPnameCbo')
        self.pidLineEdit = self.findChild(QLineEdit, 'pidLineEdit')
        self.pnameLineEdit = self.findChild(QLineEdit, 'pnameLineEdit')
        self.pdescLineEdit = self.findChild(QLineEdit, 'pdescLineEdit')
        self.ppriceLineEdit = self.findChild(QLineEdit, 'ppriceLineEdit')
        self.pqtyLineEdit = self.findChild(QLineEdit, 'pqtyLineEdit')
        self.vidLineEdit = self.findChild(QLineEdit, 'vidLineEdit')
        self.peditBtn = self.findChild(QPushButton, 'peditBtn')
        self.pdelBtn = self.findChild(QPushButton, 'pdelBtn')

        # Add Product
        self.apnameLineEdit = self.findChild(QLineEdit, 'apnameLineEdit')
        self.apdescLineEdit = self.findChild(QLineEdit, 'apdescLineEdit')
        self.appriceLineEdit = self.findChild(QLineEdit, 'appriceLineEdit')
        self.apqtyLineEdit = self.findChild(QLineEdit, 'apqtyLineEdit')
        self.avidLineEdit = self.findChild(QLineEdit, 'avidLineEdit')
        self.aaddProductBtn = self.findChild(QPushButton, 'aaddProductBtn')

    def coAddBtnClickHandler(self):
        pass

    def coUpBtnClickHandler(self):
        pass

    def coDownBtnClickHandler(self):
        pass

    def coDeleteBtnClickHandler(self):
        pass

    def coCOnfirmClickHandler(self):
        pass

    def peditBtnClickHandler(self):
        pass

    def pdelBtnClickHandler(self):
        pass

    def aaddProductBtnClickHandler(self):
        pass

    def initializeCustomers(self):
        self.acfnameLineEdit = self.findChild(QLineEdit, 'acfnameLineEdit')
        self.aclnameLineEdit = self.findChild(QLineEdit, 'aclnameLineEdit')
        self.acaddressLineEdit = self.findChild(QLineEdit, 'acaddressLineEdit')
        self.acemailLineEdit = self.findChild(QLineEdit, 'acemailLineEdit')
        self.acphoneLineEdit = self.findChild(QLineEdit, 'acphoneLineEdit')
        self.acBtn = self.findChild(QPushButton, 'acBtn')
        self.acBtn.clicked.connect(self.acBtnClickHandler)
        self.acLabel = self.findChild(QLabel, 'acLabel')

        self.eccidLineEdit = self.findChild(QLineEdit, 'eccidLineEdit')
        self.ecfnameLineEdit = self.findChild(QLineEdit, 'ecfnameLineEdit')
        self.eclnameLineEdit = self.findChild(QLineEdit, 'eclnameLineEdit')
        self.ecaddressLineEdit = self.findChild(QLineEdit, 'ecaddressLineEdit')
        self.ecemailLineEdit = self.findChild(QLineEdit, 'ecemailLineEdit')
        self.ecphoneLineEdit = self.findChild(QLineEdit, 'ecphoneLineEdit')
        self.ecBtn = self.findChild(QPushButton, 'ecBtn')
        self.ecBtn.clicked.connect(self.ecBtnClickHandler)
        self.ecLabel = self.findChild(QLabel, 'ecLabel')

    def initializeManager(self):
        self.initializeInvoicesTable()
        self.initializeActiveCustomersTable()
        self.initializeOutOfStockTable()

    def acBtnClickHandler(self):
        try:
            fname = self.acfnameLineEdit.text()
            lname = self.aclnameLineEdit.text()
            address = self.acaddressLineEdit.text()
            email = self.acemailLineEdit.text()
            phone = self.acphoneLineEdit.text()
            result = addCustomer(fname, lname, address, email, phone)
        except Exception as e:
            self.acLabel.setText(str(e))
        else:
            if result == 1:
                self.acLabel.setText('Customer added')
            else:
                self.acLabel.setText('Customer not added')

        self.refreshCustomersTab()

    def ecBtnClickHandler(self):
        try:
            cid = self.eccidLineEdit.text()
            fname = self.ecfnameLineEdit.text()
            lname = self.eclnameLineEdit.text()
            address = self.ecaddressLineEdit.text()
            email = self.ecemailLineEdit.text()
            phone = self.ecphoneLineEdit.text()
            result = editCustomer(cid, fname, lname, address, email, phone)
        except Exception as e:
            self.ecLabel.setText(str(e))
        else:
            if result == 1:
                self.ecLabel.setText('Customer updated')
            else:
                self.ecLabel.setText('Customer not updated')
        self.refreshCustomersTab()

    def refreshCustomersTab(self):
        self.acfnameLineEdit.clear()
        self.aclnameLineEdit.clear()
        self.acaddressLineEdit.clear()
        self.acemailLineEdit.clear()
        self.acphoneLineEdit.clear()

        self.eccidLineEdit.clear()
        self.ecfnameLineEdit.clear()
        self.eclnameLineEdit.clear()
        self.ecaddressLineEdit.clear()
        self.ecemailLineEdit.clear()
        self.ecphoneLineEdit.clear()

    def initializeInvoicesTable(self):
        self.invoicesTableWidget = self.findChild(QTableWidget, 'invoicesTableWidget')
        colNames, data = getInvoices()
        self.displayInvoiceDataInTable(colNames, data, self.invoicesTableWidget)

    def initializeActiveCustomersTable(self):
        self.activeTableWidget = self.findChild(QTableWidget, 'activeTableWidget')
        colNames, data = getActiveCustomers()
        self.displayInvoiceDataInTable(colNames, data, self.activeTableWidget)

    def initializeOutOfStockTable(self):
        self.outOfStockTable = self.findChild(QTableWidget, 'outOfStockTable')
        colNames, data = getOutOfStock()
        self.displayStockDataInTable(colNames, data, self.outOfStockTable)

    def displayInvoiceDataInTable(self, columns, rows, table: QTableWidget):
        table.setRowCount(len(rows))
        table.setColumnCount(len(columns))
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
        columns = ['Invoice_ID', 'Customer_ID', 'Invoice_Total', 'Date']
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))

    def displayActiveCustomersInTable(self, columns, rows, table: QTableWidget):
        table.setRowCount(len(rows))
        table.setColumnCount(len(columns))
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
        columns = ['Customer_ID', 'Last_Purchase']
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))

    def displayStockDataInTable(self, columns, rows, table: QTableWidget):
        table.setRowCount(len(rows))
        table.setColumnCount(len(columns))
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
        columns = ['Product_ID', 'Product_Name', 'Description', 'Vendor_ID', 'Quantity', 'Price']
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

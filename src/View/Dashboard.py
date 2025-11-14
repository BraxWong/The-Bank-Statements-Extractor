from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QGraphicsDropShadowEffect, QFileDialog
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QFont
from Controller.TransactionEntriesController import *
from Util.Parser import *
from CustomComponents.CustomDialog import *

class Dashboard(QWidget):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Dashboard")
        self.username = username
        self.transaction_entries_controller = TransactionEntriesController()
        transactions = self.transaction_entries_controller.get_transaction_entries_based_on_username(self.username)
        while transactions is None:
            dialog = CustomDialog('Missing Data', 'I noticed that you have not enter any data into system. Please select a bank statement to continue.')
            dialog.exec()
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Open File",
                "", 
                "Text files (*.pdf);;All files (*.*)"
            )
            if file_path:
                parser = Parser(file_path, self.username)
                parser.parse()
                transactions = self.transaction_entries_controller.get_transaction_entries_based_on_username(self.username)
            else:
                dialog = CustomDialog('Error', 'Please select a valid bank statement.')
                dialog.exec()
        #TODO: Create a UI for the dashboard
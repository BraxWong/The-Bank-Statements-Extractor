from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QGraphicsDropShadowEffect, QFileDialog
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QFont
from Controller.TransactionEntriesController import *
from Util.Parser import *

class Dashboard(QWidget):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Dashboard")
        self.username = username
        self.transaction_entries_controller = TransactionEntriesController()
        transactions = self.transaction_entries_controller.get_transaction_entries_based_on_username(self.username)
        if transactions is None:
            #TODO: Show files picker
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Open File",
                "", 
                "Text files (*.pdf);;All files (*.*)"
            )
            if file_path:
                parser = Parser(file_path, self.username)
                parser.parse()
        else:
            #TODO: Create a UI for the dashboard
            pass
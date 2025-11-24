from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QGraphicsDropShadowEffect, QFileDialog, QGridLayout, QTableWidget,
    QTableWidgetItem
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QFont
from Controller.UserSettingsController import *
from Controller.TransactionEntriesController import *
from Util.Parser import *
from CustomComponents.CustomDialog import *
from CustomComponents.Card import *
import datetime

class Dashboard(QWidget):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Dashboard")
        self.username = username
        self.user_settings_controller = UserSettingsController()
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

        grid_layout = QGridLayout()

        # Bank Account Balance Section
        self.user_settings = self.user_settings_controller.get_user_settings_based_on_username(self.username)
        self.bank_balance = self.user_settings.get_bank_account_balance()

        bank_account_balance = Card()
        bank_account_balance.setFixedSize(QSize(600, 600)) 
        bank_account_layout = QFormLayout()
        
        bank_account_balance_title_label = QLabel("Bank Account Balance")
        bank_account_balance_title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bank_account_balance_title_label.setStyleSheet("border: none;")
        font = QFont("sans-serif", 26) 
        font.setBold(True)
        bank_account_balance_title_label.setFont(font)
        
        bank_account_balance_label = QLabel("$" + str(self.bank_balance))
        bank_account_balance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bank_account_balance_label.setStyleSheet("border: none;")
        font = QFont("sans-serif", 36) 
        font.setBold(True)
        bank_account_balance_label.setFont(font)


        bank_account_layout.addRow(bank_account_balance_title_label)
        bank_account_layout.addRow(bank_account_balance_label)

        bank_account_balance.setLayout(bank_account_layout)

        grid_layout.addWidget(bank_account_balance, 0, 0)

        # Users Budgets ie: Monthly savings, Salary...
        user_budget = Card()
        user_budget.setFixedSize(QSize(600, 600))
        user_budget_layout = QFormLayout()

        user_budget_title_label = QLabel("Monthly Budget")
        user_budget_title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        user_budget_title_label.setStyleSheet("border: none;")
        font = QFont("sans-serif", 26) 
        font.setBold(True)
        user_budget_title_label.setFont(font)

        user_budget_layout.addRow(user_budget_title_label)

        user_budget.setLayout(user_budget_layout)
        grid_layout.addWidget(user_budget, 0, 1)


        # User's Financial Goals Display
        financial_goals_display = Card()
        financial_goals_display.setFixedSize(QSize(600, 600))
        financial_goals_layout = QFormLayout()

        financial_goals_title_label = QLabel("Financial Goals")
        financial_goals_title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        financial_goals_title_label.setStyleSheet("border: none;")
        font = QFont("sans-serif", 26) 
        font.setBold(True)
        financial_goals_title_label.setFont(font)

        financial_goals_layout.addRow(financial_goals_title_label)

        financial_goals_display.setLayout(financial_goals_layout)
        grid_layout.addWidget(financial_goals_display, 1, 0)


        # User's Monthly Spending
        monthly_spending = Card()
        monthly_spending.setFixedSize(QSize(600, 600))
        monthly_spending_layout = QFormLayout()

        monthly_spending_title_label = QLabel("Monthly Spending")
        monthly_spending_title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        monthly_spending_title_label.setStyleSheet("border: none;")
        font = QFont("sans-serif", 26) 
        font.setBold(True)
        monthly_spending_title_label.setFont(font)

        monthly_spending_table = QTableWidget(len(transactions), 5)
        monthly_spending_table.setFixedSize(550, 300)

        # Setting the header 
        headers = ["Item Number", "Date", "Description", "Amount", "Category"]
        for i in range(len(headers)):
            monthly_spending_table.setItem(0, i, QTableWidgetItem(headers[i]))

        # Setting table items
        for i in range(len(transactions)):
            monthly_spending_table.setItem(i + 1, 0, QTableWidgetItem(str(i)))
            monthly_spending_table.setItem(i + 1, 1, QTableWidgetItem(transactions[i].date))
            monthly_spending_table.setItem(i + 1, 2, QTableWidgetItem(transactions[i].description))
            monthly_spending_table.setItem(i + 1, 3, QTableWidgetItem(transactions[i].amount))
            monthly_spending_table.setItem(i + 1, 4, QTableWidgetItem(transactions[i].category))
        monthly_spending_table.show()
        
        monthly_spending_layout.addRow(monthly_spending_title_label)
        monthly_spending_layout.addRow(monthly_spending_table)

        monthly_spending.setLayout(monthly_spending_layout)
        grid_layout.addWidget(monthly_spending, 1, 1)

        self.setLayout(grid_layout)

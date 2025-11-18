import sqlite3
from Model.UserSettingsModel import *
from Model.FinancialGoalModel import *
from Controller.FinancialGoalsController import *
import Util.Util as util

class UserSettingsController:

    def __init__(self):
        self.PATHTOSQLDIR=util.getOSDBPath()
        self.con=sqlite3.connect(self.PATHTOSQLDIR+'/UserSettingsController.db')
        self.cur=self.con.cursor()
        self.create_user_settings_table()
        self.financial_goals_controller = FinancialGoalsController()

    def create_user_settings_table(self):
        self.cur.execute(
            '''
                CREATE TABLE IF NOT EXISTS UserSettings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    monthly_spending_percentage REAL NOT NULL,
                    monthly_saving_percentage REAL NOT NULL,
                    monthly_income REAL NOT NULL,
                    bank_account_balance REAL NOT NULL,
                    notification_enabled BOOLEAN NOT NULL,
                    backup_enabled BOOLEAN NOT NULL
                )
            '''
        )

    
    def get_user_settings_based_on_username(self, username):
        self.cur.execute('SELECT * FROM UserSettings WHERE username = ?', (username,))
        info = self.cur.fetchone()
        if info is None:
            return None
        user_id = info[0]
        financial_goals = self.financial_goals_controller.get_financial_goals(user_id)
        return UserSettingsModel(info[1], financial_goals, info[2], info[3], info[4], info[5], info[6], info[7])

    def add_financial_goal(self, username, goal, achieved = False):
        self.cur.execute('SELECT * FROM UserSettings WHERE username = ?', (username,))
        info = self.cur.fetchone()
        if info is None:
            return False
        self.financial_goals_controller.add_financial_goal(info[0], goal, achieved)
        return True

    def set_user_settings_based_on_username(self, username, monthly_spending_percentage, monthly_saving_percentage, monthly_income, bank_account_balance, notification_enabled, backup_enabled):
        self.cur.execute(
            '''
            INSERT INTO UserSettings (username, monthly_spending_percentage, monthly_saving_percentage, monthly_income, bank_account_balance, notification_enabled, backup_enabled)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (username, monthly_spending_percentage, monthly_saving_percentage, monthly_income, bank_account_balance, notification_enabled, backup_enabled)
        )
        self.con.commit()

    def update_user_settings_based_on_username(self, username, monthly_spending_percentage, monthly_saving_percentage, monthly_income, bank_account_balance, notification_enabled, backup_enabled):
        self.cur.execute(
            f'UPDATE UserSettings SET monthly_spending_percentage = ? AND monthly_saving_percentage = ? AND monthly_income = ? AND bank_account_balance = ? AND notification_enabled = ? AND backup_enabled = ? WHERE username = ?', (monthly_spending_percentage, monthly_saving_percentage, monthly_income, bank_account_balance, notification_enabled, backup_enabled, username)
        )
        self.con.commit()

    def update_bank_account_balance_based_on_username(self, username, bank_account_balance):
        self.cur.execute(
            f'UPDATE UserSettings SET bank_account_balance = ? WHERE username = ?', (bank_account_balance, username)
        )
        self.con.commit()
import sqlite3
from Model.FinancialGoalModel import *
import Util.Util as util

class FinancialGoalsController:

    def __init__(self):
        self.PATHTOSQLDIR=util.getOSDBPath()
        self.con=sqlite3.connect(self.PATHTOSQLDIR+'/FinancialGoalsController.db')
        self.cur=self.con.cursor()
        self.create_financial_goals_table()

    def create_financial_goals_table(self):
        self.cur.execute(
            '''
                CREATE TABLE IF NOT EXISTS FinancialGoals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    goal TEXT NOT NULL,
                    achieved BOOLEAN NOT NULL,
                    user_settings_id INTEGER,
                    FOREIGN KEY (user_settings_id) REFERENCES UserSettings (id) ON DELETE CASCADE
                )
            '''
        )

    def add_financial_goal(self, user_settings_id, goal, achieved = False):
        self.cur.execute(
            f'INSERT INTO FinancialGoals (goal, achieved, user_settings_id) VALUES("{goal}", "{achieved}", "{user_settings_id}")'
        )
        self.con.commit()

    def get_financial_goals(self, user_settings_id):
        self.cur.execute(
            f'SELECT * FROM FinancialGoals WHERE user_settings_id'
        )
        info = self.cur.fetchall()
        financial_goals = []
        for goal in info:
            financial_goals.append(FinancialGoal(goal[1], goal[2]))
        return financial_goals
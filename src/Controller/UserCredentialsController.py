import sqlite3
import Util.Util as util
from Model.UserCredentialsModel import *

class UserCredentialsController:

    def __init__(self):
        self.PATHTOSQLDIR=util.getOSDBPath()
        self.con=sqlite3.connect(self.PATHTOSQLDIR+'/UserCredentialsController.db')
        self.cur=self.con.cursor()
        self.create_user_credentials_table()

    def create_user_credentials_table(self):
        self.cur.execute(
            "CREATE TABLE if not exists UserCredentials(email, username, password, hint)"
        )
    
    def get_user_credentials_based_on_username(self, username):
        self.cur.execute(
            f'SELECT * FROM UserCredentials WHERE username = "{username}"'
        )
        info = self.cur.fetchone()
        if info is None:
            return None
        return UserCredentialsModel(info[0][0], info[0][1], info[0][2], info[0][3])

    def add_user_credentials(self, email, username, password, hint):
        self.cur.execute(
            f'INSERT INTO UserCredentials VALUES("{email}", "{username}", "{password}", "{hint}")'
        )
        self.con.commit()

    def remove_credentials_based_on_username(self, username):
        self.cur.execute(
            f'DELETE * FROM UserCredentials WHERE username = "{username}"'
        )
        self.con.commit()

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
        self.cur.execute('SELECT * FROM UserCredentials WHERE username = ?', (username,))
        info = self.cur.fetchone()
        if info is None:
            return None
        return UserCredentialsModel(info[0], info[1], info[2], info[3])
        
    def login_validation(self, username, password):
        self.cur.execute('SELECT * FROM UserCredentials WHERE username = ? AND password = ?', (username, password))
        info = self.cur.fetchone()
        if info is None:
            return None
        return UserCredentialsModel(info[0], info[1], info[2], info[3])

    def add_user_credentials(self, email, username, password, hint):
        self.cur.execute(
            f'INSERT INTO UserCredentials VALUES("{email}", "{username}", "{password}", "{hint}")'
        )
        self.con.commit()

    def remove_credentials_based_on_username(self, username):
        self.cur.execute(
            f'DELETE FROM UserCredentials WHERE username = "{username}"'
        )
        self.con.commit()

    def change_user_password_hint(self, email, password, hint):
        self.cur.execute(
            f'UPDATE UserCredentials SET password = ? AND hint = ? WHERE email = ?', (password, hint, email)
        )
        self.con.commit()

    def get_all_credentials(self):
        self.cur.execute(
            f'SELECT * FROM UserCredentials'
        )
        info = self.cur.fetchall()
        user_credentials = []
        for credential in info:
            user_credentials.append(UserCredentialsModel(credential[0], credential[1], credential[2], credential[3]))
        return user_credentials
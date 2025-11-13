from Model.TransactionEntriesModel import *
import sqlite3
import Util.Util as util

class TransactionEntriesController:
    def __init__(self):
        self.PATHTOSQLDIR=util.getOSDBPath()
        self.con=sqlite3.connect(self.PATHTOSQLDIR+'/TransactionEntries.db')
        self.cur=self.con.cursor()
        self.create_transaction_entries_table()

    def create_transaction_entries_table(self):
        self.cur.execute(
            "CREATE TABLE if not exists TransactionEntries(username, amount, category, date, description)"
        )
    
    def get_transaction_entries_based_on_username(self, username):
        self.cur.execute('SELECT * FROM TransactionEntries WHERE username = ?', (username,))
        info = self.cur.fetchall()
        if not len(info): return None
        transactions = []
        for transaction in info:
            transactions.append(TransactionEntriesModel(transaction[1], transaction[2], transaction[3], transaction[4]))
        return transactions
        
    def add_transaction_entry(self, username, amount, category, date, description):
        self.cur.execute(
            f'INSERT INTO TransactionEntries VALUES("{username}", "{amount}", "{category}", "{date}", "{description}")'
        )
        self.con.commit()

    def get_all_credentials(self):
        self.cur.execute(
            f'SELECT * FROM TransactionEntries'
        )
        info = self.cur.fetchall()
        transactions = []
        for transaction in info:
            transactions.append(TransactionEntriesModel(transaction[1], transaction[2], transaction[3], transaction[4]))
        return transactions

    def is_entry_in_db(self, username, amount, category, date, description):
        self.cur.execute(
            'SELECT * FROM TransactionEntries WHERE username = ? AND amount = ? AND category = ? AND date = ? AND description = ?', 
            (username, amount, category, date, description)
        )
        info = self.cur.fetchone()
        return info != None
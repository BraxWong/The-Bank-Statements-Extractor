class UserSettingsModel:

    def __init__(self, username, financial_goals, monthly_spending_percentage, monthly_saving_percentage, monthly_income, bank_account_balance, notification_enabled, backup_enabled):
        self.username = username
        self.financial_goals = financial_goals
        self.monthly_spending_percentage = monthly_spending_percentage
        self.monthly_saving_percentage = monthly_saving_percentage
        self.monthly_income = monthly_income
        self.bank_account_balance = bank_account_balance
        self.notification_enabled = notification_enabled
        self.backup_enabled = backup_enabled

    def set_username(self, username):
        self.username = username

    def set_financial_goals(self, financial_goals):
        self.financial_goals = financial_goals

    def set_monthly_spending_percentage(self, monthly_spending_percentage):
        self.monthly_spending_percentage = monthly_spending_percentage

    def set_monthly_saving_percentage(self, monthly_saving_percentage):
        self.monthly_saving_percentage = monthly_saving_percentage

    def set_monthly_income(self, monthly_income):
        self.monthly_income = monthly_income

    def set_bank_account_balance(self, bank_account_balance):
        self.bank_account_balance = bank_account_balance

    def set_notification_enabled(self, notification_enabled):
        self.notification_enabled = notification_enabled

    def set_backup_enabled(self, backup_enabled):
        self.backup_enabled = backup_enabled

    def get_username(self):
        return self.username

    def get_financial_goals(self):
        return self.financial_goals

    def get_monthly_spending_percentage(self):
        return self.monthly_spending_percentage

    def get_monthly_saving_percentage(self):
        return self.monthly_saving_percentage

    def get_monthly_income(self):
        return self.monthly_income

    def get_bank_account_balance(self):
        return self.bank_account_balance

    def get_notification_enabled(self):
        return self.notification_enabled

    def get_backup_enabled(self):
        return self.backup_enabled

    def to_string(self):
        return f'Username: {self.username} | Financial Goals: {self.financial_goals} | Monthly Spending Percentage: {str(int(self.monthly_spending_percentage) * 100) + '%'} | Monthly Saving Percentage: {str(int(self.monthly_saving_percentage) * 100) + '%'} | Monthly Income: {self.monthly_income} | Bank Account Balance: {self.bank_account_balance} | Notification Enabled: {self.notification_enabled} | Backup Enabled: {self.backup_enabled}'
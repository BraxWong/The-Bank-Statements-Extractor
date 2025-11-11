class TransactionEntriesModel:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def get_amount(self):
        return self.amount

    def get_category(self):
        return self.category

    def get_date(self):
        return self.date

    def get_description(self):
        return self.description

    def set_amount(amount):
        self.amount = amount

    def set_category(category):
        self.category = category

    def set_date(date):
        self.date = date

    def set_description(description):
        self.description = description

    def to_string(self):
        return f'Date: {self.date} | Description: {self.description} | Category: {self.category} | Amount: {self.amount}'
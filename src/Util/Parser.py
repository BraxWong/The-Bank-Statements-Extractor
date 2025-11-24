import pymupdf
from datetime import datetime
from Controller.TransactionEntriesController import *
from Controller.UserSettingsController import *
from Util.Util import *
import joblib

class Parser:

    def __init__(self, file_location, username):
        self.file_location = file_location
        self.username = username
        self.transaction_entries_controller = TransactionEntriesController()
        self.user_settings_controller = UserSettingsController()
        self.date = ''

    def parse(self):
        reader = pymupdf.open(self.file_location)
        text_lines = []
        for page in reader: 
            text_lines.extend(page.get_text().splitlines())
        for i in range(len(text_lines)):
            if "Page 1" in text_lines[i]:
                self.date = self.get_date(text_lines[i+1])
            elif "Net Position" in text_lines[i]:
                account_balance = convert_currency_string_to_float(text_lines[i+1])
                self.user_settings_controller.update_bank_account_balance_based_on_username(self.username, account_balance)
            elif "HSBC One Account Transaction History" in text_lines[i]:
                self.get_transaction_history(text_lines[i+7:])

    def get_date(self, text):
        months = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }
        date = text.split(" ")
        if date[1] in months:
            date_string = f'{date[2]}-{months[date[1]]}-{date[0]}'
            datetime_object = datetime.strptime(date_string, "%Y-%m-%d")
            return datetime_object

    def get_transaction_history(self, text):
        i = 0
        transaction_date = ''
        while i < len(text):
            date_info = self.parse_date(text[i])
            if date_info[0]:
                transaction_date = str(self.date.year) + "-" + date_info[1]
                print(transaction_date)
            #End of page footer, ignore the next 14 lines of text
            elif "The Hongkong and Shanghai Banking Corporation Limited" in text[i]:
                i += 14
            #HKD Current Transaction History Header, ignore the next 6 lines of text
            elif "HKD Current" in text[i]:
                i += 6
            #Foreign Currency Savings Transaction History Header, ignore the next 8 lines of text
            elif "Foreign Currency Savings" in text[i]:
                i += 8
            #End of all transaction history
            elif "Important Notice" in text[i]:
                return
            #Seeing transaction amount. Ignore this line
            elif is_transaction_amount(text[i]):
                i += 1
                continue
            else:
                print(f'About to unpack: {text[i]}')
                i = self.unpack_singular_transaction(transaction_date, text[i:i+4], i)
                continue
            i += 1

    def parse_date(self, text):
        pattern = r'^(0?[1-9]|[12][0-9]|3[01])\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)$'
    
        match = re.match(pattern, text)
        
        if match:
            day = match.group(1)
            
            months = {
                "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
                "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
                "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
            }
            
            month_name = match.group(2) 
            month_number = months[month_name] 
            
            return [True,f"{month_number}-{day}"]
        else:
            return [False, None]

    def unpack_singular_transaction(self, date, text, idx):
        transaction_description = ''
        transaction_amount = ''
        transaction_category = ''
        line_skipped = 0
        for i in range(len(text)):
            if i == 0:
                # B/F BALANCE ... IRRELEVANT INFO
                if "B/F BALANCE" in text[i]:
                    return idx + 2
                # CASH REBATE ... IRRELEVANT INFO
                elif "CASH REBATE" in text[i]:
                    return idx + 4
                else:
                    transaction_description = text[i]
                    line_skipped += 1
            elif i == 1:
                line_skipped += 1
                if not is_transaction_id(text[i]) and is_transaction_amount(text[i]):
                    transaction_amount = text[i]
                    if not self.transaction_entries_controller.is_entry_in_db(self.username, transaction_amount, None, date, transaction_description):
                        #TODO: The prediction model works horribly. Needs fixing
                        prediction_model = joblib.load('../src/PredictionModel/prediction_category_model.joblib')
                        try:
                            transaction_category = prediction_model.predict([text[i]])[0]
                        except Exception as e:
                            print("Unable to predict the category... Default to MISC")
                            transaction_category = "MISC"
                        self.transaction_entries_controller.add_transaction_entry(self.username, transaction_amount, transaction_category, date, transaction_description)
                    return idx + line_skipped
            elif i == 2:
                if is_transaction_amount(text[i]) and is_transaction_amount(text[i+1]):
                    line_skipped += 1
                line_skipped += 1
                transaction_amount = text[i]
                if not self.transaction_entries_controller.is_entry_in_db(self.username, transaction_amount, None, date, transaction_description):
                    try:
                        transaction_category = prediction_model.predict(text[i])
                    except Exception as e:
                        print("Unable to predict the category... Default to MISC")
                        transaction_category = "MISC"
                    self.transaction_entries_controller.add_transaction_entry(self.username, transaction_amount, transaction_category, date, transaction_description)
                return idx + line_skipped
        return 0
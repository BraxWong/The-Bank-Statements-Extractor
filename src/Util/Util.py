import platform
import os
import re

def getOSDBPath():
    OS = platform.system()
    db_directory = "Database/SQLFiles"
    if OS == "Darwin":
        db_directory = f"/tmp/{db_directory}"
    elif OS == "Windows":
        db_directory = f"C:/{db_directory}"
    else:
        db_directory = f"/var/tmp/{db_directory}"
    if not os.path.exists(db_directory):
        os.makedirs(db_directory,exist_ok=True)
    return db_directory

def check_password_strength(password):
    number_exists_in_password=False
    letters_exists_in_password=False
    upper_letters_exists_in_password=False
    symbols= {'!','@','#','$','^','&','*','?'}
    symbol_exists_in_password=False
   
    for char in password:
        if char.isdigit():
            number_exists_in_password = True
        elif char.isupper():
            upper_letters_exists_in_password = True
        elif char.islower():
            letters_exists_in_password = True
        elif char in symbols:
            symbol_exists_in_password = True
    if number_exists_in_password and letters_exists_in_password and upper_letters_exists_in_password and symbol_exists_in_password and len(password) >= 12:
        return True 
    return False

def is_transaction_id(text):
    pattern = r'^(HC\d{14})\s+(\d{2}[A-Z]{3})$'
    matches = re.findall(pattern, text, re.MULTILINE)

    return len(matches) == 2

def is_transaction_amount(text):
    pattern = r'(\d{1,3}(?:,\d{3})*\.\d{2})'
    matches = re.findall(pattern, text)
    return len(matches) == 1

def convert_currency_string_to_float(text):
    pattern = r'(\d{1,3}(?:,\d{3})*\.\d{2})'
    match = re.match(pattern, text)
    if match:
        currency_string = match.group(1).replace(',', '')
        return float(currency_string)
    else:
        return None

new_widget_reference = None
def transition_to_login_page(widget):
    from View.Login import Login
    global new_widget_reference
    new_widget_reference = Login()
    widget.close()
    new_widget_reference.show()
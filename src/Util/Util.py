import platform
import os

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

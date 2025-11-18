from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton,  QRadioButton,
    QGraphicsDropShadowEffect, 
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QFont
from CustomComponents.ClickableLabel import ClickableLabel
from CustomComponents.CustomDialog import CustomDialog
import Model.UserCredentialsModel
from Controller.UserCredentialsController import *
from Controller.UserSettingsController import *
from Util.Util import *

class SignUp(QWidget):
    def __init__(self):
        super().__init__()

        self.user_credential_controller = UserCredentialsController()
        self.user_settings_controller = UserSettingsController()

        self.setWindowTitle("Sign Up")
        self.setMinimumSize(QSize(300, 400))
        self.setStyleSheet("""
            background: qlineargradient(x1:0, y1:1, x2:1, y2:0, 
                                stop:0 #0ac2f5, stop:0.5 #aa73e6, stop:1 #f50ab2);           
        """)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setColor(QColor('#222222'))
        shadow.setOffset(0, 0)

        form_container = QWidget()
        form_container.setStyleSheet("""
            background: white; 
            border-radius: 15px;
            padding: 30px;
            min-width: 400px;
            max-width: 400px;
        """)
        form_container.setGraphicsEffect(shadow)

        form_layout = QFormLayout()

        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(lambda x:transition_to_login_page(self))
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(x1:0, y1:1, x2:1, y2:0, 
                                stop:0 #0ac2f5, stop:0.5 #aa73e6, stop:1 #f50ab2);
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                min-width: 25px;
                max-width: 50px;
            }
            
            QPushButton:hover {
                border: 2px solid #ffffff
            }
        """)
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Type your email address")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Type your username")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Type your password")
        self.hint = QLineEdit()
        self.hint.setPlaceholderText("Type your password hint")

        self.show_password_radioButton = QRadioButton("Show Password")
        self.show_password_radioButton.toggled.connect(self.update_password_visibility)

        signup_label = QLabel("Sign Up")
        signup_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("sans-serif", 28) 
        font.setBold(True)
        signup_label.setFont(font)

        self.login_button = QPushButton("SIGN UP")
        self.login_button.clicked.connect(self.handle_sign_up)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(x1:0, y1:1, x2:1, y2:0, 
                                stop:0 #0ac2f5, stop:0.5 #aa73e6, stop:1 #f50ab2);
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                min-width: 300px;
                max-width: 400px;
            }
            
            QPushButton:hover {
                border: 2px solid #ffffff
            }
        """)

        button_container = QWidget()
        button_layout = QHBoxLayout()  
        button_layout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignCenter)  
        button_layout.setContentsMargins(0, 0, 0, 0)  
        button_container.setLayout(button_layout)  

        form_layout.addRow(self.back_button)
        form_layout.addRow(signup_label)
        form_layout.addRow(QLabel("Email Address:"))
        form_layout.addRow(self.email_input)
        form_layout.addRow(QLabel("Username:"))
        form_layout.addRow(self.username_input)
        form_layout.addRow(QLabel("Password:"))
        form_layout.addRow(self.password_input)
        form_layout.addRow(QLabel("Hint:"))
        form_layout.addRow(self.hint)
        form_layout.addRow(self.show_password_radioButton)
        form_layout.addRow(button_container)
        
        layout.addWidget(form_container)
        form_container.setLayout(form_layout)

        self.setLayout(layout)

    def update_password_visibility(self):
        if self.show_password_radioButton.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_password = True
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.show_password = False

    def handle_sign_up(self):
        error_message = self.new_account_detail_validation()
        if error_message == None:
            self.user_credential_controller.add_user_credentials(self.email_input.text(), self.username_input.text(), self.password_input.text(), self.hint.text())
            self.user_settings_controller.set_user_settings_based_on_username(self.username_input.text(), 0.0, 0.0, 0.0, 0.0, False, False)
            dialog = CustomDialog("Success", "Your account has been created")
            dialog.exec()
            transition_to_login_page(self)
        else:
            dialog = CustomDialog("Error", error_message)
            dialog.exec()
            
    def new_account_detail_validation(self):
        error_message = 'Following errors have been found:\n'
        if not len(self.email_input.text()): 
            error_message += "Please provide a valid email address.\n"
        if not len(self.username_input.text()):
            error_message += "Please provide a username.\n"
        if not len(self.password_input.text()):
            error_message += "Please provide a password.\n"
        if not len(self.hint.text()):
            error_message += "Please provide a password hint.\n"
        if self.hint.text() == self.password_input.text() or self.password_input.text() in self.hint.text():
            error_message += "Password can't appear in the password hint.\n"
        if self.user_credential_controller.get_user_credentials_based_on_username(self.username_input.text()) != None:
            error_message += "Username has been used.\n"
        if not check_password_strength(self.password_input.text()):
            error_message += "Password is invalid."
        return None if error_message == 'Following errors have been found:\n' else error_message
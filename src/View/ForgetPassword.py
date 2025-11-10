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
from Util.Util import *

class ForgetPassword(QWidget):
    def __init__(self):
        super().__init__()

        self.user_credential_controller = UserCredentialsController()

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

        self.email_layout = QHBoxLayout()
        self.email_layout.setSpacing(5)
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Type your email address")
        self.email_input.setFixedWidth(100)
        self.verify_email_button = QPushButton("Verify")  
        self.verify_email_button.clicked.connect(self.verify_email_address)
        self.verify_email_button.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(x1:0, y1:1, x2:1, y2:0, 
                                stop:0 #0ac2f5, stop:0.5 #aa73e6, stop:1 #f50ab2);
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                min-width: 100px;
                max-width: 200px;
            }
            
            QPushButton:hover {
                border: 2px solid #ffffff
            }
        """)
        self.email_layout.addWidget(self.email_input)
        self.email_layout.addWidget(self.verify_email_button)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Type your new password")
        self.password_input.setEnabled(False)
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setPlaceholderText("Re-type your new password")
        self.confirm_password_input.setEnabled(False)
        self.hint = QLineEdit()
        self.hint.setPlaceholderText("Type your password hint")
        self.hint.setEnabled(False)

        self.show_password_radioButton = QRadioButton("Show Password")
        self.show_password_radioButton.toggled.connect(self.update_password_visibility)

        reset_password_label = QLabel("Reset Password")
        reset_password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("sans-serif", 28) 
        font.setBold(True)
        reset_password_label.setFont(font)

        self.reset_password_button = QPushButton("RESET PASSWORD")
        self.reset_password_button.clicked.connect(self.handle_reset_password)
        self.reset_password_button.setStyleSheet("""
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
        button_layout.addWidget(self.reset_password_button, alignment=Qt.AlignmentFlag.AlignCenter)  
        button_layout.setContentsMargins(0, 0, 0, 0)  
        button_container.setLayout(button_layout)  

        form_layout.addRow(reset_password_label)
        form_layout.addRow(QLabel("Email Address:"))
        form_layout.addRow(self.email_layout)
        form_layout.addRow(QLabel("New Password:"))
        form_layout.addRow(self.password_input)
        form_layout.addRow(QLabel("Confirm Password:"))
        form_layout.addRow(self.confirm_password_input)
        form_layout.addRow(QLabel("New Password Hint"))
        form_layout.addRow(self.hint)
        form_layout.addRow(self.show_password_radioButton)
        form_layout.addRow(button_container)
        
        layout.addWidget(form_container)
        form_container.setLayout(form_layout)

        self.setLayout(layout)

    def update_password_visibility(self):
        if self.show_password_radioButton.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_password = True
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_password = False

    def verify_email_address(self):
        user_credential = self.user_credential_controller.get_user_credentials_based_on_username(self.email_input.text())
        if user_credential:
            self.email_input.setStyleSheet("color: green;")
            self.password_input.setEnabled(True)
            self.confirm_password_input.setEnabled(True)
            self.hint.setEnabled(True)
        else:
            dialog = CustomDialog("Error", "Your email address is not found.")

    def handle_reset_password(self):
        error_message = self.new_account_detail_validation()
        if error_message == None:
            self.user_credential_controller.add_user_credentials(self.email_input.text(), self.password_input.text(), self.hint.text())
            dialog = CustomDialog("Success", "Your password has been reset")
            from View.Login import Login
            self.widget = Login()
            self.close()
            self.widget.show()
        else:
            dialog = CustomDialog("Error", error_message)

    def new_account_detail_validation(self):
        error_message = 'Following errors have been found:\n'
        if not len(self.email_input.text()): 
            error_message += "Please provide a valid email address.\n"
        if not len(self.password_input.text()):
            error_message += "Please provide a password.\n"
        if not len(self.hint.text()):
            error_message += "Please provide a password hint.\n"
        if self.password_input.text() != self.confirm_password_input.text():
            error_message += "The new password and the confirmed password has to be the same.\n"
        if self.hint.text() == self.password_input.text() or self.password_input.text() in self.hint.text():
            error_message += "Password can't appear in the password hint.\n"
        if self.user_credential_controller.get_user_credentials_based_on_username(self.username_input.text()) != None:
            error_message += "Username has been used.\n"
        if not check_password_strength(self.password_input.text()):
            error_message += "Password is invalid."
        return None if error_message == 'Following errors have been found:\n' else error_message
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QFont
from CustomComponents.ClickableLabel import ClickableLabel
import Model.UserCredentialsModel
from Controller.UserCredentialsController import *
from View.Dashboard import *


class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.user_credential_controller = UserCredentialsController()
        self.setWindowTitle("Login")
        self.setMinimumSize(QSize(300, 500))
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
            min-width: 500px;
            max-width: 500px;
        """)
        form_container.setGraphicsEffect(shadow)

        form_layout = QFormLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Type your username")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Type your password")

        self.show_password_radioButton = QRadioButton("Show Password")
        self.show_password_radioButton.toggled.connect(self.update_password_visibility)

        forget_password_label = ClickableLabel("Forget password?", self)
        forget_password_label.clicked.connect(self.forget_password)

        sign_up_label = ClickableLabel("SIGN UP", self)
        sign_up_label.clicked.connect(self.sign_up)

        login_label = QLabel("Login")
        login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("sans-serif", 28) 
        font.setBold(True)
        login_label.setFont(font)

        self.login_button = QPushButton("LOGIN")
        self.login_button.clicked.connect(self.handle_login)
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

        form_layout.addRow(login_label)
        form_layout.addRow(QLabel("Username:"))
        form_layout.addRow(self.username_input)
        form_layout.addRow(QLabel("Password:"))
        form_layout.addRow(self.password_input)
        form_layout.addRow(self.show_password_radioButton)
        form_layout.addRow(forget_password_label)
        form_layout.addRow(button_container)
        form_layout.addRow(sign_up_label)

        
        layout.addWidget(form_container)
        form_container.setLayout(form_layout)

        self.setLayout(layout)


    def handle_login(self):
        self.widget = Dashboard("350Oven")
        self.close()
        self.widget.show()
        # user_credential = self.user_credential_controller.login_validation(self.username_input.text(), self.password_input.text()) 
        # if user_credential:
        #     self.widget = Dashboard(user_credential.get_username())
        #     self.close()
        #     self.widget.show()
        # else:
        #     print("Failed")

    def update_password_visibility(self):
        if self.show_password_radioButton.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_password = True
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.show_password = False

    def forget_password(self):
        from View.ForgetPassword import ForgetPassword
        self.widget = ForgetPassword()
        self.close()
        self.widget.show()

    def sign_up(self):
        from View.SignUp import SignUp
        self.sign_up_widget = SignUp()
        self.close()
        self.sign_up_widget.show()
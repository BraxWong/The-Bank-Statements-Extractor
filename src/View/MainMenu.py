from PySide6 import QtCore, QtWidgets
import sys

class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("中天廚房設備有限公司報價單編輯器")

        self.newQuotationButton = QtWidgets.QPushButton("新報價單")
        self.newQuotationButton.clicked.connect(self.openCustomerDetails)
        
        self.exitApplicationButton = QtWidgets.QPushButton("關閉程序")
        self.exitApplicationButton.clicked.connect(self.exitApplication)
        
        self.modifyDatabaseButton = QtWidgets.QPushButton("改數據庫")
        self.modifyDatabaseButton.clicked.connect(self.openDatabaseEditor)
        
        self.text = QtWidgets.QLabel("中天廚房設備有限公司報價單編輯器",alignment=QtCore.Qt.AlignCenter)
        self.text.setStyleSheet(''' font-size: 30px; ''')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.newQuotationButton)
        self.layout.addWidget(self.modifyDatabaseButton)
        self.layout.addWidget(self.exitApplicationButton)

        container = QtWidgets.QWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

    def exitApplication(self):
        sys.exit()

    def openCustomerDetails(self):
        print("Testing")

    def openDatabaseEditor(self):
        print("More Testing")
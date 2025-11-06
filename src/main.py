from PySide6 import QtWidgets
from View.Login import Login
import sys

if __name__ == "__main__":
  
    app = QtWidgets.QApplication([])
    widget = Login()
    widget.show()
    sys.exit(app.exec())

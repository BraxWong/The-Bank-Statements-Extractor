from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QMouseEvent, QFont

class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, text="", parent=None):
        self.font = QFont("sans-serif")
        super().__init__(text, parent)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)

    def enterEvent(self, event: QMouseEvent):
        self.font.setUnderline(True)
        super().setFont(self.font)

    def leaveEvent(self, event: QMouseEvent):
        self.font.setUnderline(False)
        super().setFont(self.font)


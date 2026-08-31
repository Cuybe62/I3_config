from pathlib import Path

from PySide6.QtCore import Qt, QProcess, QTimer

from PySide6.QtWidgets import QButtonGroup


class ClipboardDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("clipBoard")
        self.setObjectName("clipboardDialog")
        self.setFixedSize(440, 330)
        self.windowFlags() | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint

        self.build_ui()
        apply_feature_style(self, __file__)

        self.update_status()

from pathlib import Path

from PySide6.QtCore import Qt, QProcess, QTimer

from PySide6.QtWidgets import (
    QButtonGroup,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
)

from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from core.system import apply_feature_style, run_script


SCREENLIGHT_SCRIPT = Path(__file__).parent / "screen.sh"
KEYBOARDLIGHT_SCRIPT = Path(__file__).parent / "keyboard.sh"
ICON_DIR = Path(__file__).parent / "src"


class BrightnessDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        # var
        self.script = SCREENLIGHT_SCRIPT

        self.setWindowTitle("Brightness")
        self.setObjectName("brightnessDialog")
        self.setFixedSize(440, 330)

        self.build_ui()
        apply_feature_style(self, __file__)

        self.update_status()

    def build_ui(self):

        self.topLayout = QVBoxLayout()
        self.topLayout.setContentsMargins(32, 28, 32, 28)
        self.topLayout.setSpacing(14)

        # -----------------------------
        #  title
        # -----------------------------
        self.title = QLabel("Contrôle de la luminosité")
        self.title.setObjectName("titleLabel")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.topLayout.addWidget(self.title)

        self.subtitle = QLabel("Choisissez une source, puis ajustez son intensité")
        self.subtitle.setObjectName("subtitleLabel")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.topLayout.addWidget(self.subtitle)

        # -----------------------------

        # -----------------------------
        #  slider
        # -----------------------------

        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setObjectName("brightnessSlider")
        self.slider.setRange(1, 100)

        self.sliderLabel = QLabel()
        self.sliderLabel.setObjectName("valueLabel")
        self.sliderLabel.setText("---")
        self.sliderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.topLayout.addWidget(self.slider)

        self.topLayout.addWidget(self.sliderLabel)
        self.slider.valueChanged.connect(self.on_slider_value_changed)

        # -----------------------------

        # -----------------------------
        #  Bouton
        # -----------------------------

        self.ButtomLayout = QHBoxLayout()
        self.ButtomLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ButtomLayout.setSpacing(18)

        self.modeButtons = QButtonGroup(self)
        self.modeButtons.setExclusive(True)

        self.ScreenBtn = QPushButton()
        self.ScreenBtn.setObjectName("modeButton")
        self.ScreenBtn.setIcon(QIcon(str(ICON_DIR / "desktop-solid-full.svg")))
        self.ScreenBtn.setIconSize(QSize(50, 50))
        self.ScreenBtn.setFixedSize(72, 72)
        self.ScreenBtn.setToolTip("Luminosité de l’écran")
        self.ScreenBtn.clicked.connect(self.on_screen_btn_clicked)
        self.modeButtons.addButton(self.ScreenBtn)

        self.ButtomLayout.addWidget(self.ScreenBtn)

        self.KeyBoardBtn = QPushButton()
        self.KeyBoardBtn.setObjectName("modeButton")
        self.KeyBoardBtn.setIcon(QIcon(str(ICON_DIR / "keyboard-regular-full.svg")))
        self.KeyBoardBtn.setIconSize(QSize(50, 50))
        self.KeyBoardBtn.setFixedSize(72, 72)
        self.KeyBoardBtn.setToolTip("Rétroéclairage du clavier")
        self.KeyBoardBtn.clicked.connect(self.on_keyboard_btn_clicked)
        self.modeButtons.addButton(self.KeyBoardBtn)

        self.ButtomLayout.addWidget(self.KeyBoardBtn)

        self.topLayout.addLayout(self.ButtomLayout)
        self.setLayout(self.topLayout)

    def on_screen_btn_clicked(self):
        self.script = SCREENLIGHT_SCRIPT
        self.slider.setRange(1, 100)
        self.update_status()

    def on_keyboard_btn_clicked(self):
        self.script = KEYBOARDLIGHT_SCRIPT
        self.slider.setRange(1, 100)
        self.update_status()

    def on_slider_value_changed(self, value):
        process = run_script(str(self.script), "set", str(value))

        # The "set" command has no value to return. Its exit code only tells
        # us whether the command succeeded.
        if process.returncode != 0:
            self.sliderLabel.setText("Erreur lors de la modification de la valeur.")
            return

        self.sliderLabel.setText(f"Valeur actuelle: {value}")

    def update_status(self):
        result = run_script(str(self.script), "status")
        value = result.stdout.strip()

        try:
            value = int(value)
            self.slider.blockSignals(True)
            self.slider.setValue(value)
            self.slider.blockSignals(False)
            self.sliderLabel.setText(f"Valeur actuelle: {value}")
        except ValueError:
            self.sliderLabel.setText("Erreur lors de la récupération de la valeur.")

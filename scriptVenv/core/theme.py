from pathlib import Path
from tempfile import gettempdir

from qt_material import apply_stylesheet

STYLE_PATH = Path(__file__).parent.parent / "styles" / "main.qss"
ICON_CACHE = Path(gettempdir()) / "qt-material-icons"


def apply_theme(app):
    apply_stylesheet(
        app,
        theme="dark_blue.xml",
        parent=str(ICON_CACHE),
    )

    if STYLE_PATH.is_file():
        custom_style = STYLE_PATH.read_text(encoding="utf-8")
        app.setStyleSheet(f"{app.styleSheet()}\n{custom_style}")

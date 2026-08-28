import subprocess
from pathlib import Path


def run_command(command):
    return subprocess.run(command, capture_output=True, text=True)


def run_script(script, *arguments):
    return subprocess.run([script, *arguments], capture_output=True, text=True)


def apply_feature_style(widget, feature_file, style_path="src/style.qss"):
    """Load and apply a QSS file relative to a feature module."""
    stylesheet_path = Path(feature_file).resolve().parent / style_path

    if not stylesheet_path.is_file():
        raise FileNotFoundError(f"Feature stylesheet not found: {stylesheet_path}")

    widget.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

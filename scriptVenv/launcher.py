import sys

from PySide6.QtWidgets import QApplication

from core.theme import apply_theme

from features.brightness.feature import BrightnessFeature


FEATURES = {"brightness": BrightnessFeature, "clipboard": clipboardFeature}


def main():

    if len(sys.argv) < 2:

        print("Usage: python launcher.py <feature>")

        print("\nFeatures disponibles:")

        for feature in FEATURES:
            print(f" - {feature}")

        sys.exit(1)

    feature_name = sys.argv[1]

    if feature_name not in FEATURES:

        print(f"Feature inconnue : {feature_name}")

        sys.exit(1)

    # -------------------------
    # QApplication
    # -------------------------

    app = QApplication(sys.argv)

    # -------------------------
    # Qt Material
    # -------------------------

    apply_theme(app)

    # -------------------------
    # Feature
    # -------------------------

    feature_class = FEATURES[feature_name]

    feature = feature_class()

    window = feature.create_window()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

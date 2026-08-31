from core.feature import Feature
from features.brightness.dialogue import BrightnessDialog


class clipBoardFeature(Feature):

    name = "Clipboard"
    title = "Presse-papier"
    description = "Gestion du presse-papier intéractif"

    def create_window(self):
        return ClipboardDialog()

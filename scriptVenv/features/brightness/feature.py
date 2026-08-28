from core.feature import Feature
from features.brightness.dialogue import BrightnessDialog


class BrightnessFeature(Feature):

    name = "Brightness"
    title = "Luminosité"
    description = "Contrôle de la luminosité "

    def create_window(self):
        return BrightnessDialog()

# Get Clicker instance
from src.Clicker import clicker

from src.interval import getInterval


class Button():
    def __init__(self, entries):
        self.entries = entries
        self.active = False

    def startButton(self):
        if self.active:
            self.active = False
            clicker.deactivate()
        else:
            self.active = True
            seconds = getInterval(self.entries)
            clicker.interval = seconds
            clicker.activate()

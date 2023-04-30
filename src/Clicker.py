# To simulate clicks
import pyautogui

# To use time intervals
from src.interval import getInterval
import time

# To toggle the clicker
import keyboard


pyautogui.FAILSAFE = True
HOTKEY = 'f6'


class Clicker():
    def __init__(self):
        self.previousClick = time.time()
        self.interval = 1
        self.active = False

    def listen(self, button, entries):
        if self.active:
            button['text'] = 'Stop (F6)'
            self.click()
        else:
            button['text'] = 'Start (F6)'

        print("Listening")
        if keyboard.is_pressed(HOTKEY):
            print("Hotkey pressed")
            self.interval = getInterval(entries)
            self.toggle()

    def click(self):
        if time.time() - self.previousClick >= self.interval:
            print("Left click")
            self.previousClick = time.time()
            pyautogui.leftClick()

    def activate(self):
        print("Activated")
        self.previousClick = time.time()
        self.active = True

    def deactivate(self):
        print("Deactivated")
        self.active = False

    def toggle(self):
        if self.active:
            self.deactivate()
        else:
            self.activate()


clicker = Clicker()

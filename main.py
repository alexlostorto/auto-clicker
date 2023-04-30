# For Python GUI
import tkinter as tk

# Simplify GUI creation
from src.MainWindow import Window

# Separate button functionality
from src.buttons import Button

# Create Clicker instance
from src.Clicker import clicker

# Slow down the main loop
import time

# Create window Tkinter
window = tk.Tk()
window.title(" Auto Clicker ")
window.geometry("500x300")
window.minsize(500, 300)
window.maxsize(700, 500)

# Create GUI geometry
headerFrame = Window(window).HorizontalFrame(height=60)
intervalsFrame = Window(window).HorizontalFrame(height=100)
buttonFrame = Window(window).HorizontalFrame(height=100)

# Create GUI elements
headerLabel = Window(headerFrame).Label(text="Auto Clicker", font='Calibri 20 bold')
hoursEntry = Window(intervalsFrame).Entry(relx=0.25, rely=0.6, anchor=tk.CENTER)
minutesEntry = Window(intervalsFrame).Entry(relx=0.5, rely=0.6, anchor=tk.CENTER)
secondsEntry = Window(intervalsFrame).Entry(relx=0.75, rely=0.6, anchor=tk.CENTER)
hoursLabel = Window(intervalsFrame).Label(relx=0.25, rely=0.3, anchor=tk.CENTER, text="Hours", font='Calibri 12 bold')
minutesLabel = Window(intervalsFrame).Label(relx=0.5, rely=0.3, anchor=tk.CENTER, text="Minutes", font='Calibri 12 bold')
secondsLabel = Window(intervalsFrame).Label(relx=0.75, rely=0.3, anchor=tk.CENTER, text="Seconds", font='Calibri 12 bold')
startButton = Window(buttonFrame).Button(text="Start (F6)", command=Button(entries=[hoursEntry, minutesEntry, secondsEntry]).startButton, font='Calibri 15')


if __name__ == '__main__':
    while True:
        time.sleep(0.05)
        window.update_idletasks()
        window.update()
        clicker.listen(startButton, [hoursEntry, minutesEntry, secondsEntry])

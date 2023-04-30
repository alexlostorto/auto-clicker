# To edit tkinter entries
import tkinter as tk


def returnInt(text):
    text = text.replace(' ', '')
    text = text.replace(',', '')
    if text.isdigit():
        return int(text)
    elif text == '':
        return 0
    else:
        return False


def getInterval(entries):
    hours = returnInt(entries[0].get())
    minutes = returnInt(entries[1].get())
    seconds = returnInt(entries[2].get())
    seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

    if seconds < 1:
        print("Interval can't be less than 1 second")
        entries[2].delete(0, tk.END)
        entries[2].insert(0, '1')
        return 1

    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

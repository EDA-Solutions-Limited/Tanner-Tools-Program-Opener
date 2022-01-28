import os
import platform
import sys

import PySimpleGUI as sg
import pyautogui

from layout import Layout

version_code = __version__ = "2.0"

op_sys = platform.system().lower()  # Current operating system in lower case
popenericon = os.path.abspath("popener.ico")


def get_size_layout():
    if op_sys == "windows":
        sizelayout = (390, 430)
    elif op_sys == "linux":
        sizelayout = (500, 430)
    else:
        sizelayout = (390, 430)
    return sizelayout


def get_gui_position():
    layoutWidth, layoutHeight = get_size_layout()
    screenWidth, screenHeight = pyautogui.size()

    progWidth = (screenWidth - layoutWidth) / 2
    progHeight = (screenHeight - layoutHeight) / 2

    return progWidth, progHeight


prevWinLoc = get_gui_position() # Previous window location on screen

# window manager class
class WindowManager:
    def __init__(self, layout: Layout):
        self.window_manager = layout
# function to create a new window, calls the layout class to build the window contents
    def new_window(self):
        global prevWinLoc
        sizelayout = get_size_layout()
        window: object = sg.Window('Program Opener ' + version_code, margins=(3, 2),
                                   layout=self.window_manager.generate_layout(),
                                   background_color="#272533", size=sizelayout, return_keyboard_events=False,
                                   location=prevWinLoc, icon=popenericon)

        event, values = window.read()

        if event is None:
            window.close()
            sys.exit()
        else:
            prevWinLoc = window.CurrentLocation()
            window.close()
            return event

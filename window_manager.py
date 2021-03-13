import os
import platform
import sys

import PySimpleGUI as sg
import pyautogui
from layout import Layout
version_code = __version__ = "1.0.5"

op_sys = platform.system().lower()  # Current operating system in lower case
popenericon = os.path.dirname(__file__) + '\popener.ico'


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


class WindowManager:
    def __init__(self,layout:Layout):
        self.window_manager = layout
        self.prevWinLoc = get_gui_position()

    def new_window(self):
        #self.window_manager.generate_layout
        sizelayout = get_size_layout()
        window: object = sg.Window('Program Opener ' + version_code, margins=(3, 2), layout= self.window_manager.generate_layout(),
                                   background_color="#272533", size=sizelayout, return_keyboard_events=False,
                                   location=self.prevWinLoc, icon=popenericon)

        event, values = window.read()

        if event is None:
            window.close()
            sys.exit()
        else:
            self.prevWinLoc = window.CurrentLocation()
            window.close()
            return event

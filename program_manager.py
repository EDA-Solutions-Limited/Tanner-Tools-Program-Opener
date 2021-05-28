import os
import platform  # Used to get the current operating system
import subprocess  # used to open programs in windows.
from sys import exit
from tkinter.filedialog import test
from os.path import isfile
from file_manager import FileManager
from layout import Layout
from window_manager import WindowManager

file_manager = FileManager()
op_sys = platform.system().lower()  # Current operating system in lower case
global prevWinLoc

if not isfile("data.json"):
    file_manager.write_json(file_manager.find_tanner(file_manager.windows_MentorGraphics))
test_dict = file_manager.load_json()

def choose_program():
    prog = ["nothing", "L-Edit", "S-Edit", "T-Spice", "WaveformViewer", "TannerDesigner",
            "LibManager"]  # Initialised list for programs
    progWindow = WindowManager(
        Layout("What program would you like to open?", prog))
    chosen_prog = progWindow.new_window()

    if chosen_prog != "Back":
        return choose_year(chosen_prog)
    else:
        return "Back", "Back","Back"

def choose_year(chosen_prog):
    years = sorted([item for item in test_dict.keys()],reverse=True)
    years.insert(0,"nothing")
    yearWindow = WindowManager(
        Layout("What year would you like to open?", years))
    chosen_year = yearWindow.new_window()
    if chosen_year != "Back":
        return choose_version(chosen_prog, chosen_year)
    else:
        return choose_program()

def choose_version(chosen_prog, chosen_year):
    versions = sorted([item for item in test_dict[chosen_year].keys()], reverse=True)
    versions.insert(0, "nothing")
    versWindow = WindowManager(
        Layout("What version would you like to open? ", versions))
    chosen_version = versWindow.new_window()
    if chosen_version != "Back":
        return chosen_prog, chosen_year,chosen_version
    else:
        return choose_year(chosen_prog)


def open_program(chosen_prog, chosen_year, chosen_version):
    version_path = test_dict[chosen_year][chosen_version]["Installation path"]

    programsDictWindows = {"nothing": "nothing", "L-Edit": "ledit64.exe", "S-Edit": "sedit64.exe",
                           "T-Spice": "tspice64.exe", "WaveformViewer": "WaveformViewer64.exe",
                           "TannerDesigner": "tdesigner64.exe", "LibManager": "libmgr64.exe"}
    programsDictLinux = {"nothing": "nothing", "L-Edit": "ledit", "S-Edit": "sedit", "T-Spice": "tspice",
                         "WaveformViewer": "WaveformViewer", "TannerDesigner": "tdesigner", "LibManager": "libmgr"}

    if op_sys == "windows":
        subprocess.Popen(
            [version_path + "\\" + programsDictWindows[chosen_prog], '-new-tab'])

    elif op_sys == "linux":  # #Choose the different OS ways of opening the programs. If not coded, ERROR 003
        # Since this machine is using modules, this has been addressed.
        os.system("module unload tanner; module load tanner/" + chosen_version + "; " + programsDictLinux[
            chosen_prog] + "&")

    else:  # #Exception of "op_sys == "
        print("ERROR 0003 \t This OS is not supported: " + op_sys + "\n")
        exit()

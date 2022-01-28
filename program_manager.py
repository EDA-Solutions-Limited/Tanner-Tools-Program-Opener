import os
import platform  # Used to get the current operating system
import subprocess  # used to open programs in windows.
from sys import exit
from os.path import isfile
from file_manager import FileManager, write_json, find_tanner, load_json
from layout import Layout
from window_manager import WindowManager

file_manager = FileManager()
op_sys = platform.system().lower()  # Current operating system in lower case
global prevWinLoc
# check if a a json file with all programs exists, if not create one
if not isfile("data.json"):
    write_json(find_tanner(file_manager.windows_MentorGraphics))
test_dict = load_json()
# function to update the json file with the new program at runtime
def update_versions():
    global test_dict
    write_json(find_tanner(file_manager.windows_MentorGraphics))
    test_dict = load_json()


def choose_program():
    prog = ["nothing", "L-Edit", "S-Edit", "T-Spice", "WaveformViewer", "TannerDesigner",
            "LibManager"]  # Initialised list for programs
    prog_window = WindowManager(
        Layout("What program would you like to open?", prog))
    chosen_prog = prog_window.new_window() # returns what the user chose, a program or "Back"

    if chosen_prog != "Back": # If the user didnt click on Back, and chooses a program, proceed to the next step (Years)
        return choose_year(chosen_prog)
    else: # If the user clicked on Back, return to the home page
        return "Back", "Back", "Back"


def choose_year(chosen_prog):
    years = sorted([item for item in test_dict.keys()], reverse=True) # Sorted list of years, latest at top
    years.insert(0, "nothing") # Insert "nothing" as the first item in the list, Pysimple GUI requires this
    year_window = WindowManager(
        Layout("What year would you like to open?", years))
    chosen_year = year_window.new_window() # returns what the user chose, a year or "Back"
    if chosen_year != "Back": # If the user didnt click on Back, and chooses a year, proceed to the next step (Versions)
        return choose_version(chosen_prog, chosen_year)
    else: # If the user clicked on Back, return to the previous step
        return choose_program()


def choose_version(chosen_prog, chosen_year):
    versions = sorted([item for item in test_dict[chosen_year].keys()], reverse=True) # Sorted list of versions, latest at top
    versions.insert(0, "nothing") # Insert "nothing" as the first item in the list, Pysimple GUI requires this
    version_window = WindowManager(
        Layout("What version would you like to open? ", versions))
    chosen_version = version_window.new_window() # returns what the user chose, a version or "Back"
    if chosen_version != "Back": # If the user didnt click on Back, and chooses a version, return everything the user chose to this step
        return chosen_prog, chosen_year, chosen_version
    else: # If the user clicked on Back, return to the previous step
        return choose_year(chosen_prog)


def open_program(chosen_prog, chosen_year, chosen_version):
    version_path = test_dict[chosen_year][chosen_version]["Installation path"] # Path to the version of the program

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

from file_manager import FileManager
from window_manager import WindowManager
import os
import platform  # Used to get the current operating system
from sys import exit
from layout import Layout
import subprocess  # used to open programs in windows.
file_manager = FileManager()
op_sys = platform.system().lower()  # Current operating system in lower case
def choose_program():
    prog = ["nothing", "L-Edit", "S-Edit", "T-Spice", "WaveformViewer", "TannerDesigner",
            "LibManager"]  # Initialised list for programs
    progWindow = WindowManager(
        Layout("What program would you like to open?", prog))
    chosen_prog = progWindow.new_window()

    if chosen_prog != "Back":
        return chosen_prog
    else:
        return "Back"


def choose_version():
    versWindow = WindowManager(
        Layout("What version would you like to open? ", file_manager.find_tanner(op_sys)))
    chosen_version = versWindow.new_window()
    if chosen_version != "Back":
        return chosen_version
    else:
        return choose_program()


def open(chosen_prog, chosen_version):
    version_path = file_manager.findVersion_path(chosen_version, op_sys)

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

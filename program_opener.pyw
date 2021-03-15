#!/usr/bin/env python
import platform  # Used to get the current operating system

from dockings import Docking
from file_manager import FileManager
from layout import Layout
from program_manager import choose_program, choose_version, open_program
from window_manager import WindowManager, get_gui_position

__author__ = "Airam Perez Guillen & James Mutumba"
__copyright__ = "Copyright 2021, James Mutumba, EDA Solutions LTD"


# ###These are the paths there the available versions will be fetched from.
op_sys = platform.system().lower()  # Current operating system in lower case
dockings = Docking(FileManager())
prevWinLoc = get_gui_position()
yes_no = ["nothing", "yes", "no"]  # List for yes/no

optionsOpen = ["nothing", "open program", "new docking", "delete old docking", "exit"]  # Options of main menu
optionOpenChosen = "nothing"  # initialised the last chosen option to open variable

lastprogramchosen = "none"  # Initialised Last Chosen Program

while optionOpenChosen != "exit":  # menu
    open_window = WindowManager(
        Layout("What would you like to do? ", optionsOpen))
    if (len(
            optionsOpen) > 3):  # If the options are more than just open and close and nothing.
        optionOpenChosen = open_window.new_window()
    else:
        optionOpenChosen = "open program"

    if optionOpenChosen == "open program":
        chosen_prog = choose_program()
        if chosen_prog == "Back":
            continue
        chosen_version = choose_version()
        while chosen_version == "Back":
            chosen_prog = choose_program()
            if chosen_prog == "Back":
                break
            chosen_version = choose_version()
        if chosen_prog == "Back":
            continue
        lastprogramchosen = "Again " + chosen_prog + " " + chosen_version
        open_program(chosen_prog, chosen_version)
        optionsOpen = ["nothing", lastprogramchosen, "open program",
                       "new docking", "delete old docking", "exit"]

    elif optionOpenChosen == "Back":
        optionOpenChosen = open_window.new_window()
    elif optionOpenChosen == lastprogramchosen:
        open_program(chosen_prog, chosen_version)

    elif optionOpenChosen == "new docking":
        dockings.new_docking(op_sys)

    elif optionOpenChosen == "delete old docking":
        dockings.delete_old_docking(op_sys)

#!/usr/bin/env python
import platform  # Used to get the current operating system

from dockings import Docking
from file_manager import FileManager
from layout import Layout
from program_manager import choose_program, open_program , update_versions
from window_manager import WindowManager, get_gui_position

__author__ = "Airam Perez Guillen & James Mutumba"
__copyright__ = "Copyright 2021, James Mutumba, EDA Solutions LTD"


# ###These are the paths there the available versions will be fetched from.
op_sys = platform.system().lower()  # Current operating system in lower case
dockings = Docking(FileManager())
prevWinLoc = get_gui_position()
yes_no = ["nothing", "yes", "no"]  # List for yes/no
optionsOpen = ["nothing", "open program", "new docking", "delete old docking","Update Versions", "exit"]  # Options of main menu
optionOpenChosen = "nothing"  # initialised the last chosen option to open variable

lastprogramchosen = "none"  # Initialised Last Chosen Program

# ###This is the main menu of the program
if __name__ == "__main__":
    while optionOpenChosen != "exit":  # menu
        open_window = WindowManager(
            Layout("What would you like to do? ", optionsOpen))
        optionOpenChosen = open_window.new_window()

        if optionOpenChosen == "open program":
            chosen_prog, chosen_year, chosen_version = choose_program() # chosen program, year and version
            if chosen_prog == "Back": # if the user wants to go back to the main menu
                continue
            lastprogramchosen = f"Again {chosen_prog} {chosen_version}"
            open_program(chosen_prog, chosen_year, chosen_version)
            optionsOpen = ["nothing", lastprogramchosen, "open program",
                        "new docking", "delete old docking", "Update Versions", "exit"]

        elif optionOpenChosen == "Back": # if the user wants to go back to the main menu
            optionOpenChosen = open_window.new_window()
        elif optionOpenChosen == lastprogramchosen:
            open_program(chosen_prog, chosen_year, chosen_version)

        elif optionOpenChosen == "new docking":
            dockings.new_docking(op_sys)
        elif optionOpenChosen == "Update Versions":
            update_versions() # Update the versions of the programs during runtime
        elif optionOpenChosen == "delete old docking":
            dockings.delete_old_docking(op_sys)

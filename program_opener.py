#!/usr/bin/env python
__author__ = "Airam Perez Guillen & James Mutumba"
__copyright__ = "Copyright 2021, James Mutumba, EDA Solutions LTD"
#       Purpose: GUI program opener
version_code = __version__ = "1.0.7"

# When creating exe or bin, use: "pyinstaller --onefile --icon=<icon> <path to pyw>"
"""################################################################################################ NOTES START 

    04/02/2020 BETA 0.1.1: 
            Disabled docking temporarily with "".
            Added Lib Manager
            Added check so that if dockings are disabled, proceed to open program section. TEMPORARY.
            Added nicer names (instead of ledit, L-Edit)
    04/02/2020 BETA 0.1.2:
            Fixed Linux part to work with sourcing files. This does not work but changes were made in how programs and versions are read. 
    04/02/2020 BETA 0.1.3:
            Commented code.
            Simplified "lastprogramchosen" by removing redundant code.
            Fixed docking issue.
    (05-11)/02/2020 BETA 0.1.4:
            Fixed remove docking (not working on 0.1.3)
            Linux program opening fixed
    (11-12)/02/2020 BETA 0.1.5:
            Added counter function (not in use)
            Fixed remove old doking bug
            Fixed .wine-tanner folder.
            Fixed program opening screen bug - linux twice same version. -> changed location of vers = ["nothing"]
    13/02/2020 BETA 0.2:
            Fixed: Remember position of window 
            https://github.com/PySimpleGUI/PySimpleGUI/issues/829
    13/02/2020 Release 1.0.0:
            Tool finished and released
    13/02/2020 Release 1.0.1:
            Fixed Linux bug with size of GUI due to the the fonts having different spacings in the different OSs.
    18/03/2020 Release 1.0.2:
            Added support for different size screens.
            EH 005 Added program Icon.
    20/04/2020 Release 1.0.3:
            DR 001 Fixed 2020.1u4 not coming up -> (listofstuff[11]) not present.
            Started EH 001 Added back button although not coded or enabled yet (1/2)
    29/04/2020 Release 1.0.4:
            Implemented EH 001 Add back button on open program.
                Done by adding flags and functions to open_program()
            Implemented EH 003 Add latest version order.
                >Organise the tools by latest version first.
                Done by using sorted() function in find_tanner().
            Started EH 002 Add Support for many different versions of the tools.
                >Whenever we have too many versions of the tools, we need to change page or scroll up and down.
                Changed the way elements are counted.
    30/04/2020 Release 1.0.5:    
            Implemented EH 002 Add Support for many different versions of the tools.
                >Whenever we have too many versions of the tools, we need to change page or scroll up and down.
                Added columns "col" and "top". top contains the "Back" button and the question, and col contains the buttons.
            Added support for up to 50 versions of the same tool (up from 18)
    xx/xx/2020 Release 1.0.6:
            EH 002 Add Support for many different versions of the tools.
                >Whenever we have too many versions of the tools, we need to change page or scroll up and down.
            EH 004 Add system independent tool support.
                >Make the program compatible with different os architectures (i.e. Mentorgraphics in C: o D: or with a "Tanner" folder, etc.)
            Documentation link:
                https://realpython.com/documenting-python-code/

            
"""  # ############################################################################################### NOTES END
"""################################################################################################ INSTRUCTIONS START 

 1. To modify the name of the database with the paths to the docking and instal location, change them in the top of "Program opener code" section.

"""  # ############################################################################################### INSTRUCTIONS END
################################################################################################### Program GUI START.

import platform  # Used to get the current operating system
from pythonds.basic import Stack
from layout import Layout
from window_manager import WindowManager
from file_manager import FileManager
from dockings import Docking
from program_manager import choose_program, choose_version,open


# #-----WINDOW AND LAYOUT---------------------------------##


# -----MAIN EVENT LOOP------------------------------------##

################################################################################################### Program GUI END.
################################################################################################### Program setup code START.

################################################################################################### Program setup code end.
################################################################################################### Program code start.
# ###These are the paths there the available versions will be fetched from.
op_sys = platform.system().lower()  # Current operating system in lower case
dockings = Docking(FileManager())

yes_no = ["nothing", "yes", "no"]  # List for yes/no

optionsOpen = ["nothing", "open program", "new docking", "delete old docking", "exit"]  # Options of main menu
optionOpenChosen = "nothing"  # initialised the last chosen option to open variable

lastprogramchosen = "none"  # Initialised Last Chosen Program


while optionOpenChosen != "exit":         # menu

    if (len(
            optionsOpen) > 3):  # If the options are more than just open and close and nothing.      # Choose what to do next, then iterate through the options
        
        open_window = WindowManager(
            Layout("What would you like to do? ", optionsOpen))
        optionOpenChosen = open_window.new_window()
    else:
        optionOpenChosen = "open program"

    if optionOpenChosen == "open program":
        chosen_prog = choose_program()
        if chosen_prog == "Back":
            continue
        chosen_version = choose_version()
        lastprogramchosen = "Again " + chosen_prog + " " + chosen_version
        open(chosen_prog, chosen_version)
        optionsOpen = ["nothing", lastprogramchosen, "open program",
                       "new docking", "delete old docking", "exit"]

    elif optionOpenChosen == "Back":
        optionOpenChosen = open_window.new_window()
    elif optionOpenChosen == lastprogramchosen:
        open(chosen_prog, chosen_version)

    elif optionOpenChosen == "new docking":
        dockings.new_docking(op_sys)

    elif optionOpenChosen == "delete old docking":
        dockings.delete_old_docking(op_sys)

################################################################################################### Program code end.

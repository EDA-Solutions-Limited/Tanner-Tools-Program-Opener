
#!/usr/bin/env python
__author__ = "Airam Perez Guillen"
__copyright__ = "Copyright 2020, Airam Perez Guillen, EDA Solutions LTD"
#       Purpose: GUI program opener
version_code = __version__ = "WIP1.0.6"

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
            Fixed remove old docking bug
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
    13/07/2020 Release 1.0.6:
                DR 005 Open again button is broken

    xx/xx/2020 Release 1.0.7:
            EH 002 Add Support for many different versions of the tools.
                >Whenever we have too many versions of the tools, we need to change page or scroll up and down.
            EH 004 Add system independent tool support.
                >Make the program compatible with different os architectures (i.e. Mentorgraphics in C: o D: or with a "Tanner" folder, etc.)
            DR 002 When clicking back on main menu, the scroll bar appears.
            DR 003 When pressing back after choosing a version, we should be able to choose a different version again, but instead it does nothing.
            DR 004 Versions with two digits (i.e. 2016u11) are placed before single digit versions.
            EH 006 Gather usage stats. 
                >Would create a folder un %appdata% and write how mny times the program is used every day.
            DR 005 Open again button is broken
            EH 007 Capitalise the options.
                >Options are in lower case.
            EH 008 Add a "are you sure?" question on new/delete old docking, with "Yeas" and "Back" options.
                >Currently if you click by mistake it just performs the action.
            Documentation link:
                https://realpython.com/documenting-python-code/

            
"""  # ############################################################################################### NOTES END
"""################################################################################################ INSTRUCTIONS START 

 1. To modify the name of the database with the paths to the docking and instal location, change them in the top of "Program opener code" section.

"""  # ############################################################################################### INSTRUCTIONS END
# ################################################################################################## Program GUI START.

import PySimpleGUI as sg  # used to create the gui
import sys  # used to handle errors.
import platform  # Used to get the current operating system

import time  # used to sleep
from datetime import datetime  # used to print the date
import logging  # used to print log files

import os  # used to open programs in linux.
import subprocess  # used to open programs in windows.
import fnmatch  # used to match words and modify the names of the old docking files.
from pythonds.basic import Stack
import pyautogui  # Used to check the screen size

import string
from tkinter import filedialog
from tkinter import *
from configparser import ConfigParser

op_sys = platform.system().lower()  # Current operating system in lower case

# from data import images
config = ConfigParser()
popenericon = os.path.dirname(__file__) + '\popener.ico'
# popenericon = images

if os.path.isfile(popenericon):
    pass
else:
    pass
    #sg.Print('Cannot Find ICO File')



def ensure_51_spaces(
        list_provided, item_number):  # This function appends empty characters ("") so that the number of elements in the list is at least 30.
    if item_number < 51:  # 19 in order to account for "nothing"
        for x in range(51 - item_number):
            list_provided.append("")
    return list_provided


# #-----WINDOW AND LAYOUT---------------------------------##
sg.change_look_and_feel('Dark Blue 3')  # Change the look and feel of the window


def generate_layout(text, listofstuff):

    # listofstuff = [str(i) for i in range(51)]
    # ["nothing", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", ""]
 
    if len(listofstuff) <= 19:  # If everything fits in one screen, hide the scroll bars
        scrollable_flag = False
    elif 19 < len(listofstuff) <= 51:   # item_count > 19 and item_count <= 37
        scrollable_flag = True
    else:
        print("This is actually a problem and it will not be displayed correctly. :~/")

    #listofstuff = ensure_51_spaces(listofstuff, item_count)  # Fix the "list of stuff" so that there are "" appended.

    def generate_button(
            stuffinlist):  # Adds the text to be displayed on the button (Which is also the value of the button), and gives it properties (size, visibility..)
        # #-----DEFAULT SETTINGS--------------------------##
        button_visib: dict = {'size': (19, 1), 'font': ('Franklin Gothic Book', 12),
                              'button_color': ("black", "#F8F8F8"), 'visible': True}  # Visible button
        button_visib_over: dict = {'size': (19, 2), 'font': ('Franklin Gothic Book', 12),
                                   'button_color': ("black", "#F8F8F8"), 'visible': True}  # Over sized button
        button_invis: dict = {'size': (19, 1), 'font': ('Franklin Gothic Book', 12),
                              'button_color': ("black", "#F8F8F8"), 'visible': False}  # Invisible button

        if (stuffinlist != ""):  # If not an empty character, we read it.
            if (len(stuffinlist) > 25):  # If string is too long, we make the box double

                return sg.Button(stuffinlist, **button_visib_over)
            else:
                return sg.Button(stuffinlist, **button_visib)
        else:  # If it is an empty character, we turn the visibility off
            return sg.Button(stuffinlist, **button_invis)

            # Properties of the buttons
    

    # This is the column with the choices

    col = []
    for i in range (1,len(listofstuff),2):
        if i+1 <= len(listofstuff)-1:
            col +=[[generate_button(listofstuff[i]),generate_button(listofstuff[i+1])]]
        else:
            col +=[[generate_button(listofstuff[i]),generate_button("")]]

    top = [[sg.Button("Back", size=(5,1), font=('Franklin Gothic Book', 12), button_color=("black", "#84848a"), visible=True),
                 sg.Text(text, size=(34, 1), justification='right', background_color="#272533",  # Layer 2:  text question (variable) and back button
                 text_color='white', font=('Franklin Gothic Book', 12))]]

    # This is the layout of the GUI
    layout: list = [
        [sg.Text('Program Opener ' + version_code, size=(50, 1), justification='right', background_color="#272533",
                 # Layer 1:  Program opener <version>
                 text_color='white', font=('Franklin Gothic Book', 12, 'bold'))],
        [sg.Column(top, background_color="#272533")],
        [sg.Column(col, size=(390, 400), background_color="#272533", scrollable=scrollable_flag, vertical_scroll_only=scrollable_flag)]

    ]
    return layout


# -----MAIN EVENT LOOP------------------------------------##
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
    print(pyautogui.size())
    # if screenHeight == 1080:
    #     return (765, 325)

    progWidth = (screenWidth - layoutWidth) / 2
    progHeight = (screenHeight - layoutHeight) / 2

    return (progWidth, progHeight)


prevWinLoc = get_gui_position()


def new_window(text, varRead):  # Start or refresh the window(Text for the window, list of things)
    global prevWinLoc
    sizelayout = get_size_layout()
    window: object = sg.Window('Program Opener ' + version_code, margins=(3, 2), layout=generate_layout(text, varRead),
                               background_color="#272533", size=sizelayout, return_keyboard_events=False,
                               location=prevWinLoc, icon=popenericon)

    event, values = window.read()

    if event is None:
        window.close()
        sys.exit()
    else:
        prevWinLoc = window.CurrentLocation()
        print("DEBUG: Window location: " + str(prevWinLoc))
        window.close()
        return (event)


################################################################################################### Program GUI END.
################################################################################################### Program setup code START.

################################################################################################### Program setup code end.
################################################################################################### Program code start.

def write_config(path):
    config.read('config.ini')
    config.add_section('Mentor Path')
    config.set('Mentor Path', 'path', path)
    with open('config.ini', 'w') as f:
        config.write(f)

def scan_drive():

    if os.path.exists('config.ini'):
        config.read('config.ini')
        return config.get('Mentor Path','path')

    available_drives = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    toplev = 'Programs'
    Secondlev = 'MentorGraphics'
    for drive in available_drives:
        for root, subdirs, files in os.walk(drive,topdown = True):
            if toplev in subdirs:
                subdirs[:] = [toplev]
            elif ((root.find(toplev) != -1) and (Secondlev in subdirs)):
                subdirs[:] = [Secondlev]
            elif (root == (drive + toplev + "\\" + Secondlev) ):
                write_config(root)
                return root
            else:
                break      
            
    return (get_directory(toplev,Secondlev))
   

def get_directory(toplev, Secondlev):
    diag = Tk()
    diag.withdraw()

    root = filedialog.askdirectory(title = "Choose directory where tanner versions folders are located")
    if root == "":
        sys.exit()
    while ((root.find(toplev) == -1) or (root.find(Secondlev) == -1)):
        root = filedialog.askdirectory(title = "Choose directory where tanner versions folders are located")
    
    if root.endswith(Secondlev):
        write_config(root)
        return root  
    else:
        return (get_directory(toplev,Secondlev))



#These are the paths there the available versions will be fetched from.
windows_MentorGraphics = scan_drive()
linux_VersPath = "/modules/tanner"

yes_no = ["nothing", "yes", "no"]  # List for yes/no


def find_mentorgraphics():
    if op_sys == "windows":
        print(os.environ["ProgramFiles(x86)"])
        print(os.environ["ProgramFiles"])
    elif op_sys == "linux":
        os.chdir(linux_VersPath)


def find_tanner():  # This function finds the available versions of the tools installed in the machine.
    vers = ["nothing"]  # Initialised list for tool versions
    if op_sys == "windows":
        os.chdir(windows_MentorGraphics)
    elif op_sys == "linux":
        os.chdir(linux_VersPath)

    for f in os.listdir():
        if fnmatch.fnmatch(f, "20*"):
            vers.append(f)
    return sorted(vers, reverse=True)
    # End find_tanner()


def count_dots(string):  # This function counts the dots in the provided string
    d = {}
    for c in string:
        if c == "." in d:
            d[c] += 1
        else:
            d[c] = 1
    return d["."]


# ###These are the paths where the docking will be fetched from.
def getDockingPath():
    if op_sys == "windows":
        appdata_path = os.getenv('APPDATA')
        docking_path = appdata_path + "\\Tanner EDA"
    elif op_sys == "linux":
        user = os.environ.get('USER')
        versions = find_tanner()
        versions.pop(0)
        docking_path = [
            ("/home/" + user + "/.wine-tanner" + "_" + n + "/drive_c/users/" + user + "/Application Data/Tanner_EDA")
            for n in versions]
        print(docking_path)
    else:
        docking_path = "Your operating system is not supported"
        print("ERROR 0003 \t This OS is not supported: " + op_sys + "\n")
        sys.exit()
    return (docking_path)
    # end getDockingPath()


def renameOldDocking(
        docking_path):  # new docking         #This method renames the dockinglayout files by appending ".old" to the end of them.

    os.chdir(
        docking_path)  # Change the current working directory to the directory of the docking layout. This doesnt affect STATUS BAR!!!

    for f in os.listdir():  # Goes through all the files in the directory.
        if fnmatch.fnmatch(f, '*DockingLayout*'):  # Finds all matches and renames them
            try:
                new_f = f + ".old"
                print("DEBUG: " + f + " changing to " + new_f)
                os.rename(f, new_f)
            except FileExistsError:
                new_f = new_f + ".old"
                print("DEBUG: FileExistsError: " + new_f + " changing to " + new_f)
                os.rename(f, new_f)
    # printATime("\nRenamed docking files. Created temp.\n")
    # End renameOldDocking()


def renameOldDockingOld(
        docking_path):  # r emove old docking  #This method renames the dockinglayout, restoring it bu removing the ".old" at the end of them, if there is any.
    os.chdir(
        docking_path)  # Change the current working directory to the directory of the docking layout. This doesnt affect STATUS BAR!!!
    oldFlag = False  # This flag is to check if there is any ".old" file so that files do not get unnecessaryli deleted.
    m = Stack()  # This stack will contain the names of the files with ".old".
    for f in os.listdir():
        if fnmatch.fnmatch(f, '*DockingLayout*.xml.old*'):  # Find files with ".old" and push them into the stack.
            oldFlag = True
            m.push(f)
        elif oldFlag:
            oldFlag
        else:
            oldFlag = False
    print("DEBUG: \"delete old\" flag: " + str(oldFlag))
    if oldFlag:  # Only if there is a modification by this program, delete old dockings
        for f in os.listdir():
            if fnmatch.fnmatch(f,
                               '*DockingLayout*.xml'):  # First, delete the files which do not have a ".old" in them (these are the newly created ones.)
                print("DEBUG: Deleting " + f)
                os.remove(f)

        r = Stack()
        for x in sorted([m.pop() for _ in range(m.size())], key=len,
                        reverse=True):  # Sort the stck and re-stack it in a new stack called "r"
            r.push(x)

        current_popped = ''
        for _ in range(
                r.size()):  # Then, go over the ".old" files and if the file exits, the delete the existing one and rename the new one.
            current_popped = r.pop()
            try:
                new_f = current_popped.replace('.old', '')
                os.rename(current_popped, new_f)
                print("DEBUG: " + current_popped + " changing to " + new_f)
            except FileExistsError:
                os.remove(new_f)
                print(
                    "FileExistsError: Deleting " + new_f + " because " + current_popped + " would be called the same.")
                os.rename(current_popped, new_f)
                print("DEBUG: " + current_popped + " changing to " + new_f)


# ############################ DEBUG
# if count_dots(current_popped) == 2:
#     new_f = current_popped.replace('.old', '')
#     os.rename(current_popped, new_f)


# for f in os.listdir():
#     if fnmatch.fnmatch(f, '*DockingLayout*.xml.old'):
#         if count_dots(f) == 2:
#             new_f = f.replace('.old', '')
#             os.rename(f, new_f)
# for f in os.listdir():
#     if fnmatch.fnmatch(f, '*DockingLayout*.xml.old'):
#         new_f = f.replace('.old', '')
#         os.rename(f, new_f)
# for f in os.listdir():
#     if fnmatch.fnmatch(f, '*DockingLayout*.xml.old.old'):
#         new_f = f.replace('.old', '')
#         os.rename(f, new_f)
#############################
# printATime("\nRenamed old docking files... deleted temp...\n")
# End renameOldDockingOld()

optionsOpen = ["nothing", "open program", "new docking", "delete old docking", "exit"]  # Options of main menu
optionOpenChosen = "nothing"  # initialised the last chosen option to open variable

lastprogramchosen = "none"  # Initialised Last Chosen Program


def choose_program():
    prog = ["nothing", "L-Edit", "S-Edit", "T-Spice", "WaveformViewer", "TannerDesigner",
            "LibManager"]  # Initialised list for programs
    return new_window(text="What program would you like to open?",
               varRead=prog)  # choose the program for the operating system


def choose_version():
    return new_window(text="What version would you like to open? ",
                      varRead=find_tanner())  # choose the version for the program


def open_program():  # This function find the path of the tanner tools, chooses the tools and the versions to open and returns it.
    flag = True
    while flag is True:
        chosen_prog = choose_program()

        if chosen_prog == "Back":   # If Back is chosen, exit this function and pass on the while loop
            return "Back"

        chosen_version = choose_version()

        if chosen_version == "Back":   # If the button is back, we iterate again to go back
            flag = True
        elif chosen_version != "Back":  # if the button is not back, we do not iterate again and provide the answer
            flag = False

        lastprogramchosen = "Again " + chosen_prog + " " + chosen_version

        optionsOpen = ["nothing", lastprogramchosen, "open program", "new docking", "delete old docking", "exit"]

    def findVersion_path():  # Get path of installation
        if op_sys == "windows":
            os.chdir(windows_MentorGraphics + "\\" + chosen_version + "\\Tanner EDA")
            for TannerToolsV in os.listdir():  # There is only one folder here so it just returns one.
                TannerToolsV
            return (
                        windows_MentorGraphics + "\\" + chosen_version + "\\Tanner EDA\\" + TannerToolsV + "\\x64")  # Returns the RAW path
        elif op_sys == "linux":
            return (linux_VersPath + "/" + chosen_version)

    version_path = findVersion_path()

    return chosen_version, chosen_prog, version_path, optionsOpen, lastprogramchosen
    # END open_program()


while optionOpenChosen != "exit":         # menu

    if (len(
            optionsOpen) > 3):  # If the options are more than just open and close and nothing.      # Choose what to do next, then iterate through the options
        optionOpenChosen = new_window("What would you like to do? ", optionsOpen)
    else:
        optionOpenChosen = "open program"

    if optionOpenChosen == "open program" or optionOpenChosen == lastprogramchosen:
        if optionOpenChosen == "open program":
            open_program_return = open_program()

            if open_program_return == "Back":  # If back was pressed, the return wouold be "Back", and then we would pass.
                pass
            elif open_program_return != "Back":  # If back was not pressed, we carry on as usual
                chosen_version, chosen_prog, version_path, optionsOpen, lastprogramchosen = open_program_return

                programsDictWindows = {"nothing": "nothing", "L-Edit": "ledit64.exe", "S-Edit": "sedit64.exe",
                                       "T-Spice": "tspice64.exe", "WaveformViewer": "WaveformViewer64.exe",
                                       "TannerDesigner": "tdesigner64.exe", "LibManager": "libmgr64.exe"}
                programsDictLinux = {"nothing": "nothing", "L-Edit": "ledit", "S-Edit": "sedit", "T-Spice": "tspice",
                                     "WaveformViewer": "WaveformViewer", "TannerDesigner": "tdesigner", "LibManager": "libmgr"}

                if op_sys == "windows":
                    subprocess.Popen([version_path + "\\" + programsDictWindows[chosen_prog], '-new-tab'])

                elif op_sys == "linux":  # #Choose the different OS ways of opening the programs. If not coded, ERROR 003
                    # Since this machine is using modules, this has been addressed.
                    os.system("module unload tanner; module load tanner/" + chosen_version + "; " + programsDictLinux[
                            chosen_prog] + "&")

                else:  # #Exception of "op_sys == "
                    print("ERROR 0003 \t This OS is not supported: " + op_sys + "\n")
                    sys.exit()


    elif optionOpenChosen == "new docking":
        docking_path = getDockingPath()
        print("DEBUG: String? " + str(isinstance(docking_path, str)))
        print("DEBUG: List?   " + str(isinstance(docking_path, list)))
        if (isinstance(docking_path, str)):
            renameOldDocking(docking_path)
        elif (isinstance(docking_path, list)):
            for item in docking_path:
                print("DEBUG: path: " + item)
                renameOldDocking(item)

    elif optionOpenChosen == "delete old docking":
        docking_path = getDockingPath()
        print("DEBUG: String? " + str(isinstance(docking_path, str)))
        print("DEBUG: List?   " + str(isinstance(docking_path, list)))
        if (isinstance(docking_path, str)):
            renameOldDockingOld(docking_path)
        elif (isinstance(docking_path, list)):
            for item in docking_path:
                print("DEBUG: path: " + item)
                renameOldDockingOld(item)

################################################################################################### Program code end.

import string
from sys import exit
from os.path import exists
from os import walk,chdir,listdir
from tkinter import filedialog
from fnmatch import fnmatch
from tkinter import *
from configparser import ConfigParser
config = ConfigParser()

class FileManager():

    def __init__(self):
        self.windows_MentorGraphics = self.scan_drive()
        self.linux_VersPath = "/modules/tanner"


    def write_config(self,path):  # write the found path to a config file
        config.read('config.ini')
        config.add_section('Mentor Path')
        config.set('Mentor Path', 'path', path)
        with open('config.ini', 'w') as f:
            config.write(f)


    def scan_drive(self):  # scan all attached drives for mentor folder and write it to a config file

        if exists('config.ini'):
            config.read('config.ini')
            return config.get('Mentor Path', 'path')

        available_drives = ['%s:\\' % d for d in string.ascii_uppercase if exists(
            '%s:' % d)]  # create list of available drives using comprehension
        toplev = 'Programs'
        Secondlev = 'MentorGraphics'
        for drive in available_drives:
            # recursive walk of directories and subdirectories in a drive
            for root, subdirs, files in walk(drive, topdown=True):
                if toplev in subdirs:
                    # edit the subdirectories list in place to save time
                    subdirs[:] = [toplev]
                elif ((root.find(toplev) != -1) and (Secondlev in subdirs)):
                    subdirs[:] = [Secondlev]
                elif (root == (drive + toplev + "\\" + Secondlev)):  # if correct hierachy is found
                    self.write_config(root)
                    return root
                else:
                    break

        return (self.get_directory(toplev, Secondlev))


    def get_directory(self,toplev, Secondlev):
        diag = Tk()
        diag.withdraw()

        # gui to ask for location of the mentor folder
        root = filedialog.askdirectory(
            title="Choose directory where tanner versions folders are located")
        if root == "":
            exit()
        while ((root.find(toplev) == -1) or (root.find(Secondlev) == -1)):
            root = filedialog.askdirectory(
                title="Choose directory where tanner versions folders are located")

        if root.endswith(Secondlev):
            self.write_config(root)
            return root
        else:
            return (self.get_directory(toplev, Secondlev))


    # This function finds the available versions of the tools installed in the machine.
    def find_tanner(self,op_sys):
        vers = ["nothing"]  # Initialised list for tool versions
        if op_sys == "windows":
            chdir(self.windows_MentorGraphics)

        elif op_sys == "linux":
            chdir(self.linux_VersPath)
        for f in listdir():
            if fnmatch(f, "20*"):
                vers.append(f)
        return sorted(vers, reverse=True)


    def findVersion_path(self,chosen_version,op_sys):  # Get path of installation
        if op_sys == "windows":
            chdir(self.windows_MentorGraphics + "\\" +
                    chosen_version + "\\Tanner EDA")
            # There is only one folder here so it just returns one.
            for TannerToolsV in listdir():
                return (
                    self.windows_MentorGraphics + "\\" + chosen_version + "\\Tanner EDA\\" + TannerToolsV + "\\x64")  # Returns the RAW path
        elif op_sys == "linux":
            return (self.linux_VersPath + "/" + chosen_version)

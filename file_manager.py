import glob # for traversing the directory structure to find sedit.exe instances
import json # for storing the found tanner tools in a json file
from configparser import ConfigParser # for reading and writing the config file for the main Mentor path
from os.path import exists, split
from sys import exit
from tkinter import Tk # for the Mentor path location dialog
from tkinter import filedialog
from collections import defaultdict
from win32com.client import Dispatch # for getting the version number of the tanner tools
from win32api import GetFileVersionInfo

config = ConfigParser() # Create config parser object


def write_config(path):  # write the found path to a config file
    config.read('config.ini') # open the config file for writing
    config.add_section('Mentor Path')   # add a section to the config file for the Tanner tools path
    config.set('Mentor Path', 'path', path)
    with open('config.ini', 'w') as f:
        config.write(f)

# Find tanner tools path using the sedit executable(sedit.exe)
def find_tanner(root):
# glob for all sedit.exe files in the current directory, recursively search subdirectories
    text_files = glob.glob(
        root + "/**/Tanner EDA/Tanner Tools*/x64/sedit64.exe", recursive=True)
    test_dict = defaultdict(dict)
# for each sedit.exe file found, get the version number and the path, using windows File properties
    for f in text_files:
# information about windows file version info at https://docs.microsoft.com/en-us/windows/win32/menurc/versioninfo-resource
        langs = GetFileVersionInfo(text_files[0], r'\VarFileInfo\Translation')
        name_key = r'StringFileInfo\%04x%04x\ProductName' % (
            langs[0][0], langs[0][1]) # combination of the language code and the charset ID
        version_key = r'StringFileInfo\%04x%04x\ProductVersion' % (
            langs[0][0], langs[0][1]) 
        product_name = GetFileVersionInfo(f, name_key)
        major_version = GetFileVersionInfo(f, version_key)
        build = Dispatch('Scripting.FileSystemObject').GetFIleVersion(f)
# check if program is Beta or Final release using the build number, betas don't have the "Update" string in the build number
        if 'Update' not in product_name:
            test_dict['Betas'][build] = {'Installation path': split(f)[
                0], 'Name': product_name}
        else:
            test_dict[major_version.split('.')[0]][major_version] = {'Installation path': split(f)[
                0], 'Name': product_name}

    return test_dict

# write a json file containing all the paths of the tanner tools found from the find_tanner function
def write_json(test_dict):
    json_object = json.dumps(test_dict, indent=4)
    with open('data.json', 'w') as outfile:
        outfile.write(json_object)

# function to load an existing json file, saves from having to search and write each time. Faster loading
def load_json():
    with open('data.json', 'r') as openfile:
        json_object = json.load(openfile)
    return json_object

# File manager class
class FileManager:
    def __init__(self):
        self.windows_MentorGraphics = self.scan_drive()
        self.linux_VersPath = "/modules/tanner"

    def scan_drive(self):  # scan all attached drives for mentor folder and write it to a config file

        if exists('config.ini'):
            config.read('config.ini')
            return config.get('Mentor Path', 'path')

        return self.get_directory()

    def get_directory(self):
        diag = Tk()
        diag.withdraw()

        # gui to ask for location of the mentor folder
        root = filedialog.askdirectory(
            title="Choose directory where tanner versions folders are located")
        if root == "":
            exit()
        test_dict = find_tanner(root)
        if test_dict:
            write_json(test_dict)
            write_config(root)
            return root
        else:
            return self.get_directory() # recurse until the correct directory is chosen

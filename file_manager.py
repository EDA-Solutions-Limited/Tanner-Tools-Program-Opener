import glob
import json
from configparser import ConfigParser
from os import walk,sep
from os.path import exists,split
from sys import exit
from tkinter import Tk
from tkinter import filedialog
from collections import defaultdict
from win32com.client import Dispatch
from win32api import GetFileVersionInfo

config = ConfigParser()

def write_config(path):  # write the found path to a config file
    config.read('config.ini')
    config.add_section('Mentor Path')
    config.set('Mentor Path', 'path', path)
    with open('config.ini', 'w') as f:
        config.write(f)


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
        test_dict = self.find_tanner(root)
        if test_dict:
            self.write_json(test_dict)
            write_config(root)
            return root
        else:
            return self.get_directory()

    def find_tanner(self,root):

        text_files = glob.glob(
            root + "/**/Tanner EDA/Tanner Tools*/x64/sedit64.exe", recursive=True)
        test_dict = defaultdict(dict)

        for f in text_files:
            langs = GetFileVersionInfo(text_files[0], r'\VarFileInfo\Translation')
            name_key = r'StringFileInfo\%04x%04x\ProductName' % (
                langs[0][0], langs[0][1])
            version_key = r'StringFileInfo\%04x%04x\ProductVersion' % (
                langs[0][0], langs[0][1])
            product_name = GetFileVersionInfo(f, name_key)
            major_version = GetFileVersionInfo(f, version_key)
            build = Dispatch('Scripting.FileSystemObject').GetFIleVersion(f)

            if 'Update' not in product_name:
                test_dict['Betas'][build] = {'Installation path': split(f)[
                    0], 'Name': product_name}
            else:
                test_dict[major_version.split('.')[0]][major_version] = {'Installation path': split(f)[
                    0], 'Name': product_name}

        return test_dict

    def write_json(self,test_dict):
        json_object = json.dumps(test_dict, indent=4)
        with open('data.json', 'w') as outfile:
            outfile.write(json_object)

    def load_json(self):
        with open('data.json', 'r') as openfile:
            json_object = json.load(openfile)
        return json_object

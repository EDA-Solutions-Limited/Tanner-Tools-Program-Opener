import os
from fnmatch import fnmatch
from sys import exit

from pythonds.basic import Stack

from file_manager import FileManager


def rename_old_docking(docking_path):  # new docking This method renames the docking layout files by appending ".old"
    # to the end of them.

    os.chdir(
        docking_path)  # Change the current working directory to the directory of the docking layout. This doesnt
    # affect STATUS BAR!!!

    for f in os.listdir():  # Goes through all the files in the directory.
        if fnmatch(f, '*DockingLayout*'):  # Finds all matches and renames them
            try:
                new_f = f + ".old"
                print("DEBUG: " + f + " changing to " + new_f)
                os.rename(f, new_f)
            except FileExistsError:
                new_f = new_f + ".old"
                print("DEBUG: FileExistsError: " +
                      new_f + " changing to " + new_f)
                os.rename(f, new_f)
    # printATime("\nRenamed docking files. Created temp.\n")
    # End renameOldDocking()


def rename_old_docking_old(docking_path):  # remove old docking  #This method renames the dockinglayout, restoring
    # it bu removing the ".old" at the end of them, if there is any.
    os.chdir(
        docking_path)  # Change the current working directory to the directory of the docking layout. This doesnt
    # affect STATUS BAR!!!
    # This flag is to check if there is any ".old" file so that files do not get unnecessarily deleted.
    oldFlag = False
    m = Stack()  # This stack will contain the names of the files with ".old".
    for f in os.listdir():
        # Find files with ".old" and push them into the stack.
        if fnmatch(f, '*DockingLayout*.xml.old*'):
            oldFlag = True
            m.push(f)
        elif oldFlag:
            oldFlag
        else:
            oldFlag = False
    print("DEBUG: \"delete old\" flag: " + str(oldFlag))
    if oldFlag:  # Only if there is a modification by this program, delete old dockings
        for f in os.listdir():
            if fnmatch(f,
                       '*DockingLayout*.xml'):  # First, delete the files which do not have a ".old" in them (these
                # are the newly created ones.)
                print("DEBUG: Deleting " + f)
                os.remove(f)

        r = Stack()
        for x in sorted([m.pop() for _ in range(m.size())], key=len,
                        reverse=True):  # Sort the stck and re-stack it in a new stack called "r"
            r.push(x)

        current_popped = ''
        for _ in range(
                r.size()):  # Then, go over the ".old" files and if the file exits, the delete the existing one and
            # rename the new one.
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


class Docking:
    def __init__(self, file_manager: FileManager):
        self.file_manager = file_manager

    # ###These are the paths where the docking will be fetched from.

    def get_docking_path(self, op_sys):
        if op_sys == "windows":
            appdata_path = os.getenv('APPDATA')
            docking_path = appdata_path + "\\Tanner EDA"
        elif op_sys == "linux":
            user = os.environ.get('USER')
            versions = self.file_manager.find_tanner(op_sys)
            versions.pop(0)
            docking_path = [
                ("/home/" + user + "/.wine-tanner" + "_" + n +
                 "/drive_c/users/" + user + "/Application Data/Tanner_EDA")
                for n in versions]
            print(docking_path)
        else:
            docking_path = "Your operating system is not supported"
            print("ERROR 0003 \t This OS is not supported: " + op_sys + "\n")
            exit()
        return docking_path
        # end getDockingPath()

    def new_docking(self, op_sys):
        docking_path = self.get_docking_path(op_sys)

        if isinstance(docking_path, str):
            rename_old_docking(docking_path)
        elif isinstance(docking_path, list):
            for item in docking_path:
                print("DEBUG: path: " + item)
                rename_old_docking(item)

    def delete_old_docking(self, op_sys):
        docking_path = self.get_docking_path(op_sys)
        if isinstance(docking_path, str):
            rename_old_docking_old(docking_path)
        elif isinstance(docking_path, list):
            for item in docking_path:
                rename_old_docking_old(item)

# Man these imports be kinda chonky tho
from tkinter.filedialog import askopenfilenames
from time import strftime
import logging
import tkinter
import winreg
import popups
import shutil
import os

# Mandato/
os.chdir('C:/Program Files (x86)/Daniel Vahsholtz/Wallchani/file_chooser/Logs')
____lfn = strftime('%m-%d-%Y__%H;%M;%S')
logging.basicConfig(filename=____lfn + '.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(pathname)s : %(asctime)s:%(msecs)d : %(levelname)s : %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.info('Logger set up')

icon = tkinter.Tk()
icon.iconbitmap(default='C:/Code/Python/Wallchani/resources/Wallchani.ico')
icon.destroy()


def open_reg(path, name, hkey=winreg.HKEY_LOCAL_MACHINE, rights=winreg.KEY_READ):
    try:
        k = winreg.OpenKey(hkey, path, 0, rights)
        value, regtype = winreg.QueryValueEx(k, name)
        winreg.CloseKey(k)
        return value
    except Exception as e:
        # Log e
        return e

# Read registry values, and save it to a variable.


def find_folder_location():
    folder_location = open_reg(
        'SOFTWARE\\WOW6432Node\\Daniel Vahsholtz\\Wallchani', 'ImageFolderLocation')
    folder_location = "C:\\Program Files (x86)\\Daniel Vahsholtz"  # test value
    return folder_location


def open_dialog():
    enc = "utf-8"
    import sys
    try:
        import locale
        locale.setlocale(locale.LC_ALL, '')
        enc = locale.nl_langinfo(locale.CODESET)
    except (ImportError, AttributeError):
        pass
    files_to_add = askopenfilenames(filetypes=[(
        "All accepted filetypes", "*.png *.jpg *.jpeg"), ("JPEG files", "*.jpg *.jpeg"), ("PNG files", "*.png")])
    return list(files_to_add)


def calculate_total_size_of_files(list):
    total_size_of_files = 0
    for file in list:
        total_size_of_files = total_size_of_files + os.stat(file).st_size
    return total_size_of_files


def check_if_enough_space(list):
    _20_percent_of_drive = (shutil.disk_usage(find_folder_location()[:3].replace('\\', '/')).total * 0.2).__round__()

    total_size_of_files = 0

    for file in list:
        total_size_of_files = total_size_of_files + os.stat(file).st_size

    free_space = shutil.disk_usage(find_folder_location()[:3].replace('\\', '/')).free

    total_space_required = _20_percent_of_drive + total_size_of_files

    if total_space_required > free_space:
        return False
    elif total_space_required < free_space or total_space_required == free_space:
        return True
    else:
        return False


def import_file():
    file_list = open_dialog()
    if len(file_list) > 0 and check_if_enough_space(file_list):

        print(file_list)
        
        if len(file_list) > 30 or calculate_total_size_of_files(file_list) > 30720000: # (30,720,000 here is 30[ish]MB in bytes.)
            q = popups.warn_ask()
            print()
            if q == 'no':
                pass  # TODO Make program stop here
            else:
                print("Sure Thing!")

        for file in file_list:
            pass  # TODO Put copy here


if __name__ == '__main__':
    import_file()

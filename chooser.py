# Insert importing montage here
import random as rand
import configparser
import logging
import winreg
import time
import os

# TODO ADD CONFIG!!!!
# config = configparser.ConfigParser(empty_lines_in_values=False, interpolation=configparser.ExtendedInterpolation())

# An essential part of debugging: Logging.
# - Set cwd for logs to be placed
os.chdir('C:/Program Files (x86)/Daniel Vahsholtz/Wallchani/file_chooser/Logs')
# - Get a st
____lfn = time.strftime('%m-%d-%Y__%H^%M^%S')

logging.basicConfig(filename= ____lfn + '.log', encoding='utf-8', level=logging.DEBUG, format='%(pathname)s : %(asctime)s:%(msecs)d : %(levelname)s : %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.info('Logger set up')

# Starting variables
file_ext_reroll = False

# Registry reader block0
def open_reg(path, name, hkey=winreg.HKEY_LOCAL_MACHINE, rights=winreg.KEY_READ):
    try:
        k = winreg.OpenKey(hkey, path, 0, rights)
        value, regtype = winreg.QueryValueEx(k, name)
        winreg.CloseKey(k)
        return value
    except Exception as e:
        #Log e
        return e

# Read registry values, and save it to a variable.
def read_reg():
    global folder_location, walpaper_changer_location
    
    walpaper_changer_location = open_reg('SOFTWARE\\WOW6432Node\\Daniel Vahsholtz\\Wallchani', 'WallpaperChangerLocation')
    folder_location = open_reg('SOFTWARE\\WOW6432Node\\Daniel Vahsholtz\\Wallchani', 'ImageFolderLocation')

# Change cd to folder location

def change_cd():
    os.chdir(str(folder_location))

# Make a list of all the files in the directory

def file_list():
    file_list = os.listdir(path='.')
    return file_list

# Choose a random file from the file list

def pick_file():
    random_file = rand.choice(file_list())
    return random_file

# Check to see if the file ends in '.jpg', '.jpeg', or '.png' (The current accepted file types)

def check_file_ext():
    global file_ext_reroll, picked_file
    picked_file = pick_file()
    if '.png' not in picked_file:
        if '.jpg' not in picked_file:
            if '.jpeg' not in picked_file:
                file_ext_reroll = True
                file_location = str(folder_location) + '/' + picked_file
                file_location = file_location.replace('/', '\\')
                print(f'Incorrect file type/location. File name: {picked_file}. File location: {file_location}. Re-rolling.')
            else:
                file_ext_reroll = False
        else:
            file_ext_reroll = False
    else:
        file_ext_reroll = False

# Format the location of the image to the correct destination

def img_location():
    img_path_base = str(folder_location) + '/' + picked_file
    img_path_formatted = img_path_base.replace('/', '\\')
    img_path = '"' + img_path_formatted + '"'

    return img_path

# Call the wallpaper changer (Location acquired earlier from the registry if the try block is used)

def change_wallpaper():
    cl_result = os.system('wlchgr' + img_location())
    if cl_result == 1 or cl_result == 2:
        try:
            os.startfile(walpaper_changer_location, "open", img_path)# type:ignore
        except Exception as e:
            print(e)
            return e
        else:
            return True
    elif cl_result == 0:
        return True
    else:
        #Log something went wrong
        pass

# Main program
def main():
    read_reg()
    change_cd()
    pick_file()
    check_file_ext()
    while file_ext_reroll == True:
        pick_file()
        check_file_ext()
        time.sleep(0.1)

# Dev testing
if __name__ == '__main__':
    read_reg()
    change_cd()
    pick_file()
    check_file_ext()
    while file_ext_reroll == True:
        pick_file()
        check_file_ext()
        time.sleep(0.1)

    print(picked_file)
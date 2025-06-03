import shutil
import os, os.path
import time
import glob

backup_location = "C:/Users/maith/Documents/Backups/BG3/"
os.chdir(backup_location)

def create_backup():
    purge()
    list_of_files = glob.glob("C:/Users/maith/AppData/Local/Larian Studios/Baldur's Gate 3/PlayerProfiles/Public/Savegames/Story/*")
    latest_save = max(list_of_files, key=os.path.getmtime)
    tempfiles = os.path.basename(os.path.normpath(latest_save))

    timestr = time.strftime("%Y%m%d-%H%M%S")
    backup_name = backup_location + timestr

    shutil.copytree(latest_save, backup_location + 'tempfiles/' + tempfiles)
    print(f"copy to tempfiles {tempfiles}")
    shutil.make_archive(backup_name, 'zip', 'tempfiles/')
    print(f"zipped backup {backup_name}")
    shutil.rmtree('tempfiles')
    print("remove tempfiles")

def purge():
    list_of_backups = os.listdir('./')

    if (len(list_of_backups)) >= 50:
        oldest_file = min(list_of_backups, key=os.path.getctime)
        os.remove(oldest_file)
        print("deleted oldest save")
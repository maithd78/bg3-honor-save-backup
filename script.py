import shutil
import os
import time
import glob

backup_location = "C:/Users/maith/Documents/Backups/BG3/"
list_of_files = glob.glob("C:/Users/maith/AppData/Local/Larian Studios/Baldur's Gate 3/PlayerProfiles/Public/Savegames/Story/*")
latest_save = max(list_of_files, key=os.path.getmtime)

shutil.copytree(latest_save, backup_location + 'tempfiles/' + os.path.basename(os.path.normpath(latest_save)))

timestr = time.strftime("%Y%m%d-%H%M%S")
backup_name = backup_location + timestr

os.chdir(backup_location)
shutil.make_archive(backup_name, 'zip', 'tempfiles/')
shutil.rmtree('tempfiles')

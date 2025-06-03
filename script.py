import sample
import time

from sample import backup
from sample import process

def main_loop():
    while process.check_process('bg3_dx11.exe'):
        backup.create_backup()
        print("sleeping")
        time.sleep(900)
    else:
        print("Baldurs Gate 3 has stopped\nCreating last backup")
        backup.create_backup()
        input("press any key to exit")
        
if process.check_process('bg3_dx11.exe'):
    print("Baldurs Gate 3 is running.\nrunning script")
    main_loop()
else:
    print("bg3.exe is not running")
    input("press any key to exit")

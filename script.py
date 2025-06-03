import sample
import time
import subprocess

from sample import backup
from sample import process

subprocess.call(['C:/Program Files (x86)/Steam/steam.exe', '-applaunch', '1086940', '--skip-launcher'])
print("launching")
time.sleep(10)

def main_loop():
    while process.check_process('bg3_dx11.exe'):
        backup.create_backup()
        print("sleeping")
        time.sleep(900)
    else:
        print("Baldurs Gate 3 has stopped\nCreating last backup")
        backup.create_backup()
        input("press ENTER key to exit")
        
if process.check_process('bg3_dx11.exe'):
    print("Baldurs Gate 3 is running.\nrunning script")
    main_loop()
else:
    print("bg3.exe is not running")
    input("press ENTER key to exit")

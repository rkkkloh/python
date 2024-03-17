import os
import shutil

path = "text.txt"
try:
    #os.remove(path)      #delete a file
    #os.rmdir(path)       #delete an empty directory
    #shutil.rmtree(path)  #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete a folder")
except OSError:
    print("You cannot delete that with os,rmdir()")
else:
    print(path + "was deleted")
    
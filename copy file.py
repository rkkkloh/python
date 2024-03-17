# copyfile() = copies contents of a file
# сору() = copyfile() + permission mode + destination can be a directory
# copy2 () = copy () + copies metadata (file's creation and modification times)
import shutil

# shutil.copyfile("test.txt","/Users/ruikangloh//Desktop") #source,destination
# shutil.copy("test.txt","/Users/ruikangloh//Desktop") #source,destination
# shutil.copy2("test.txt","/Users/ruikangloh//Desktop") #source,destination
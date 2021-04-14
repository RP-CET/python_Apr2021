import os
import shutil

helloFile = open("myfile.txt", "w")
helloFile.write("Programming is Fun!")
helloFile.close()

os.mkdir("myfolder")
shutil.copy("myfile.txt", "myfolder/myfile.txt")
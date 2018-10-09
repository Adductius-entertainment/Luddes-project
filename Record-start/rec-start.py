import os, subprocess
from shutil import copyfile


def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)


file = newest(r"C:\Users\Ludvig\Youtube\Recorded")
filename = file.split("-'Spel'-'Med'",1)[0]


answer = input("Open latest video: ")

if answer in ['y']:
    print("Selecting", file)

answer = input("Create project: ")

name = input("Name of project: ")

if answer in ['y']:
    newpath = r'C:\Users\Ludvig\Documents\Premier projects\\' + name
    newpath1 = newpath + "\\01_Footage"
    newpath2 = newpath + "\\02_Graphics"
    newpath3 = newpath + "\\03_Audio"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        os.makedirs(newpath1)
        os.makedirs(newpath2)
        os.makedirs(newpath3)
        print(newpath + newpath1 + newpath2 + newpath3)
        copyfile(file, newpath1 + "\\" + file.split("\\")[5])
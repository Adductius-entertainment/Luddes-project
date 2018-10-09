import os
filename = ""
filenamepos = ""
yourname = "Yourname"
for file in os.listdir(r"C:\Users\Yourname\Downloads"):
    if file.endswith(".exe"):
        filename = os.path.join(r"C:\Users\" + yourname + "\Downloads", file)
        filenamepos = os.path.join(r"C:\Users\" + yourname + "\Downloads\exe", file)
        os.rename(filename, filenamepos)
    if file.endswith(".docx"):
        filename = os.path.join(r"C:\Users\" + yourname + "\Downloads", file)
        filenamepos = os.path.join(r"C:\Users\" + yourname + "\Downloads\text", file)
        os.rename(filename, filenamepos)
    if file.endswith(".png"):
        filename = os.path.join(r"C:\Users\" + yourname + "\Downloads", file)
        filenamepos = os.path.join(r"C:\Users\" + yourname + "\Downloads\images", file)
        os.rename(filename, filenamepos)
    if file.endswith(".jpg"):
        filename = os.path.join(r"C:\Users\" + yourname + "\Downloads", file)
        filenamepos = os.path.join(r"C:\Users\" + yourname + "\Downloads\images", file)
        os.rename(filename, filenamepos)
    if file.endswith(".gif"):
        filename = os.path.join(r"C:\Users\" + yourname + "\Downloads", file)
        filenamepos = os.path.join(r"C:\Users\" + yourname + "\Downloads\images", file)
        os.rename(filename, filenamepos)
    if file.endswith(".tiff"):
        filename = os.path.join(r"C:\Users\" + yourname + "\Downloads", file)
        filenamepos = os.path.join(r"C:\Users\" + yourname + "\Downloads\images", file)
        os.rename(filename, filenamepos)

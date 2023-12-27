import os

files= os.listdir()

if "main2.py" in files:
    files.remove("main2.py")
    print("true")
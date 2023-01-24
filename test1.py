import os

path = input("input the dir: ")
os.chdir(path)
for x in os.listdir(path):
    if os.path.isfile(os.path.join(path, x)):
        print(x)
    if os.path.isdir(os.path.join(path, x)):
        print(x+" (folder)")

dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
for d in dirs:
    os.rmdir(path+"/"+d)

#https://stackoverflow.com/questions/3761473/python-not-recognising-directories-os-path-isdir

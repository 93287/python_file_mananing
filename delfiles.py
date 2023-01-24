import os

see = input("do you want to see the names of the deleted files?(y/n) ")

if see == "y":
    path = input("input the dir: \n")
    os.chdir(path)
    for files in os.listdir(path):
        print(files)
    exp = input("do you wish to not delete one of those files? (y/n)")
    if exp == y:
        filexp = input("input the file's name")
        os.mkdir("not deleted files")
        os.system("mv "+filexp+" not deleted files")
    for files in os.listdir(path):
        os.remove(files)
        print(files+" has been removed.")
            
    print("\nAll files removed.")
elif see == "n":
    path = input("input the dir: \n")
    os.chdir(path)

    for files in os.listdir(path):
        os.remove(files)
           
    print("\nAll files removed.")
else:
    print("can't compute input.")

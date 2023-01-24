import os

path = input("input the dir: ")

os.chdir(path)

print("these are the files on the direction)")

for files in os.listdir(path):
	print(files)

cho = input("input the file you wish the copy: ")
num = int(input("and how  many times to copy it: "))
cop_path = input("input the dir to copy the fyle: ")



for x in range(num):
    os.system("cp "+cho+" "+cho+"_copy"+str(x))

print("done")

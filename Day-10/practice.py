import os

folders = input("provide list of folder names with spaces in between:" ).split()

for folder in folders:
    files = os.listdir(folder)
    print(files)


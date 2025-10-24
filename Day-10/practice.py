import os

folders = input("please provide list of folder names with spaces in between: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name")
        continue

    print("\n-------------listing files for the folders: " + folder, flush=True)

    for file in files:
        print(file)
    
######### 



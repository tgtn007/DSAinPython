import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("C:\\Users\\lenovo\\Desktop\\DSAinPython\\Projects\\P1\\testdir"))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))


my_dirs = os.listdir(os.getcwd())
print(my_dirs)
for dirs in my_dirs:
    if os.path.isdir(dirs):
        os.chdir(os.path.join(os.getcwd(), dirs))

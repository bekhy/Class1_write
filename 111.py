import os
name= ".py"
def dir_list(name):
    if name in os.listdir():
        for i in os.listdir(name):
            ext = i.split(".")[1]
            if ext not in dict_.keys():
    else:
        return 'Error'
print(dir_list("firstTask"))
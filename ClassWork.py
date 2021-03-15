import os

def dir_list(name):
    dict_ = {}
    if name in os.listdir():
        for i in os.listdir(name):
            ext = i.split(".")[1]
            if ext not in dict_.keys():
                dict_.update({ext:1})
            else:
                dict_.update({ext:dict_.get(ext)+1})
            return dict_
    else:
        return 'Error'
print(dir_list("firstTask"))
print(os.getcwd())
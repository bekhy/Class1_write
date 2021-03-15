# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Pres

list = [1,2,3,4,5,6,7,8,9]
def return_list (list):
    a1 = 0
    b1 = 0
    for i in list:
        if i%2 == 0:
            a1+=1
        else :
            b1+=1
    return a1, b1
a1, b1 = return_list(list)
print("Четных = " + str(a1) +" Нечетных = " + str(b1))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

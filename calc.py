# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Pres

a= float(input("Введите первое число: "))
b= float(input("Введите второе число: "))
sign = str(input("Какую операцию нужно сделать? \n+ \n- \n* \n/ \n"))
def calc (c):
    plus = "+"
    minus= "-"
    ymn="*"
    deli="/"
    if sign == plus:
        c=a+b
    elif sign == minus:
        c=a-b
    elif sign == ymn:
        c=a*b
    elif sign == deli:
        c=a/b
    else:
        print("Введен неверный символ")
    return c
print(calc(c=0))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

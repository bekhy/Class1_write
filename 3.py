# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print('Введите стороны треугольника:')
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a+b>c and b+c>a and c+a > b and a!=0 and b!= 0 and c!=0:
    print('Такой треугольник есть')
else:
    print('Треугольник не существует')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

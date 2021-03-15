# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
a= float(input("Длина коробки: "))
b= float(input("Ширина коробки: "))
c= float(input("Высота коробки: "))
m= float(input("Длина двери: "))
k= float(input("Ширина двери: "))
if (a < m and a < k and b < k and b < m
        or a < m and a < k and c < m and c < k
        or c < m and c < k and b < m and b < k):
    print("Коробка пролезет")
else:
    print("Не пролезет")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

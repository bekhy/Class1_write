class Human:
    def __init__(self, name, phone, age, city, birthday):
        self.name = name
        self.phone = phone
        self.age = age
        self.city = city
        self.birthday = birthday
    def walk(self):
        print("I can walk! ")
    def watch(self):
        print("I can see")
    def jump(self):
        print("I can jump")
    def getinfo(self):
        print(self.name)
        print(self.age)
        print(self.city)
        print(self.phone)
        print(self.birthday)

human1 = Human("Alex", "2938374823", "33", "London", "19.07.1988")
human2 = Human("Lena", "1293712983", "20", "Kiev", "27.02.2001")
human3 = Human("Dima", "7412982443", "31", "Rio-De-Janeiro", "10.01.1990")

print(human1)
human1.getinfo()
human1.walk()
human1.jump()
print("__________")
print(human2)
human2.getinfo()
human2.watch()
human2.jump()
print("----------")
human3.getinfo()
human3.walk()
human3.watch()
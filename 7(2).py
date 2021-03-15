# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

dict_a = {}
list_az = [1, 4, "3", "8", {"121":121}, {"12":12}, [1, 3, 6, 9, 12], [2, 8, 16, 32, 48]]
for i in list_az:
    if isinstance in (i, int):
        if "int" not in dict_a.keys():
            int_list = []
            int_list.append(i)
            dict_a.update({"int": int_list})
        else:
            dict_a.get("str").append(i)

#     if i in list_az == "":
#         str_a == ""
#     if i in list_az == {}:
#         dict_a == {}
#     if i in list_az == []:
#         list_z.append(i)
# print(i)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

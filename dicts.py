my_dict = {"first": "Первый", "second": "Второй", 3: "Третий"}

for k in my_dict:
    print(k, '=', my_dict[k])

print("**********перебор серез items**********")

for key, value in my_dict.items():
    print(key, ':', value)

print("*******Удаление элемента**********")

del my_dict['first']
print(my_dict)
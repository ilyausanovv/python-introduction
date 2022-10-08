lst = [1, 2, 3]

print(lst)

lst.append(5)
print(lst)

lst.remove(1)
print(lst)

print(lst[2])
print(lst)
print(lst[-2])

if 3 in lst:
    print("Цифра 3 присутствует в списке")
else:
    print("Цифра 3 отсутствует в списке")

# lst_console = input("Введите список цифр через пробел: ")
# numbers = lst_console.split(" ")
# print(numbers)

tup = (1, 2, 3)
# tup.append(5) - нельзя
# tup.remove(2) - нельзя
print(tup)

first, second, third = tup
print(first)
print(second)
print(third)

eng_rus_dict = {
    "cat": "кот",
    "car": "машина"
}

print(eng_rus_dict)
print(eng_rus_dict["cat"])
eng_rus_dict["cat"] = "Кошечка"
print(eng_rus_dict["cat"])

print("car" in eng_rus_dict)
print(eng_rus_dict.values())
print("кот" in eng_rus_dict.values())

print(eng_rus_dict.keys())
print(eng_rus_dict.items())

print(eng_rus_dict.get('brother', 'not value'))
print(eng_rus_dict.get('cat', 'not value'))

set_from_lst = set(lst)
set_example = {1, 2 ,3}
print(set_from_lst)
print(set_example)

set_example.add(5)
set_example.remove(1)
print(set_example)

print(set_example - {2, 3})
print(set_example.union({6, 7}))
print(set_example == {2, 5, 4})

print(len(set_example))
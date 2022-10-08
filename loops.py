lst2 = [1, 2, 3, 4, 5]

for item in lst2:
    print(item)

print("-" * 10)

print(range(5))
print(list(range(5)))

for i in range(5):
    if i == 2:
        break
    print(i)

print("-" * 10)

cats = ["Барсик", "Мурзик", "Василий"]
print(list(enumerate(cats)))

for indx, cat in enumerate(cats):
    print(f"{indx}. {cat}")

print(list(reversed(cats)))
print(sorted(cats))

eng_rus_dict = {
    "cat": "кошка",
    "car": "машина"
}

for key, value in eng_rus_dict.items():
    print("key: ", key, "value: ", value)

i = 0
while i != 5:
    i += 1
print(i)

print("a", ord("a"))
symbol_number = ord("a")

while symbol_number <= ord("z"):
    print(symbol_number, chr(symbol_number))
    symbol_number += 1
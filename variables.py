name = input("Введите ваше имя: ")
age = float(input("Введите ваш возраст: "))
is_working_now = input("Работаете ли вы сейчас? (1 если да, 0 если нет): ") == "1"
workplace = None

# str_template = "Информация о пользователе: {0} - {1} - {2}"
# print(str_template.format(name, age, is_working_now))

if is_working_now:
    workplace = input("Введите место работы: ")

print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Работа в данное время: {is_working_now}")

if age >= 20:
    print("Возраст пользователя больше 20-ти лет")
elif age >= 18:
    print("Пользователь совершеннолетний")
else:
    print("Пользователь несовершеннолетний")

if is_working_now:
    print("Место работы: " + workplace)

if is_working_now and not workplace:
    print("Ворнинг: не заполнено поле места работы!")
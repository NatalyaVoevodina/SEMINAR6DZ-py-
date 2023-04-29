list=[3,2,6,-9,15,20,-50,10,30,45,-60,-2]
min_number = int(input("Введите максимальное число: "))
max_number = int(input("Введите минимальное число: "))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(f"Индексы: {i}")
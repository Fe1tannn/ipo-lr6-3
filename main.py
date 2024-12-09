count = 0
list = []
quantity = int(input("Введите желаемое количество строк:"))
if quantity == 0 or quantity <1:
    print("Неверное значение")
else:
    for i in range(0, quantity):      
        list.append(str(input(f"Введите строку под номером {i + 1} ")))
joined_str = "".join(list)
split_str = joined_str.split()
lengleth = len(split_str)
count = len(set(split_str))
print(f"Rоличество строк в исходной строке   {lengleth} , количество уникальных значений в строке {count}")
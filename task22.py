first_list = set()
second_list = set()
for i in range(int(input('Введите длинну первого списка: '))):
    first_list.add(int(input('Введите число: ')))
print(first_list)
for i in range(int(input('Введите длинну второго списка: '))):
    second_list.add(int(input('Введите число: ')))

result = set.intersection(first_list,second_list)
print(sorted(result))

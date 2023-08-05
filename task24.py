bushes = int(input("Введите количество кустов: "))
blueberry = [1,2,3,4]
for i in range(bushes):
    blueberry.append(int(input(f'Введите колличество ягод на {i+1}: ')))
max_berry = 0
for i in range(len(blueberry)):
    summ = blueberry[i-2]+blueberry[i-1]+blueberry[i]
    if summ > max_berry:
        max_berry = summ
print(max_berry)
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

# n = int(input('Введите число N: '))
# nums = input("Введите список значение через пробел: ").split()
# x = int(input('Введите число X: '))
# arr = list(map(int, nums))

# for i in range(1, len(nums)):
#     if nums[i - 1] < nums[i]:
#         count += 1
# print(count)
# result = []
# for i in range(n):
#     if arr(i) == x - 1 or arr(i) == x + 1:
#         result.append(i)
# print(len(result))

# arr = []
# for i in range(n):
# #     arr.append(random.randrange(n))
# # print(arr)
# def nearval(arr, number):
#     return min(arr, key=lambda x: abs(number - abs(x))) 
# print(f'Ближайшее к {x} число в массиве: {nearval(arr, x)}')

n = abs(int(input('Введите количество элементов массива А: ')))
Ai = input("Введите целые числа: ").split()
A= list(map(int, Ai))
if len(A) != n or n == 0:
    print('Введенные элементы не соответствуют заявленному количеству')
else:
    
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - A[0])
    index = 0
    for i in range(1, n):
        count = abs(X - A[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A[index])}')
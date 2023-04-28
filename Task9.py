# Задача №9. По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# Input: 5
# Output: 120 

# n = int(input('Введите число: '))
# Factorial = 1 
# while n > 1:
#     Factorial = Factorial * n
#     n = n -1
# print('Факториал числа', Factorial)

# n = int(input('Введите число: '))
# i = 0
# Factorial = 1
# while i <= n:
#     Factorial = Factorial * n
#     n = n - 1
# print('Факториал числа', Factorial)

n = int(input())
i = 1
result = 1
while i <= n:
    result *= i
    i += 1
print(result)
# В некоторой школе решили набрать три новых математических класса и
# оборудовать кабинеты для них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

# Input:
# 20
# 21
# 22
# Output:
# 32

FirstClassPeople = int(input())
SecondClassPeople = int(input())
ThirdClassPeople = int(input())
People = int(3)
print ((FirstClassPeople + SecondClassPeople + ThirdClassPeople+1)//People) 

# ppl_on_table = 2 # колво человек за партой
# first_cl = (int(input())+1)// ppl_on_table
# second_cl = (int(input())+1)// ppl_on_table
# third_cl = (int(input())+1)// ppl_on_table
# print (first_cl+second_cl+third_cl)
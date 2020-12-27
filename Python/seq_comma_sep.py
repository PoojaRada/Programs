""" A Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple """

a = input("Enter values: ")
list = a.split(',')
tuple = tuple(list)
print(list)
print(tuple)

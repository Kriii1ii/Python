numbers = [1, 33, 11, 44, 63, 16, 55, 5, 7, 14]

#sorting
numbers.sort()
print("The sorted list is:",numbers)

#to print all of the odd numbers

odd_num = [i for i in numbers if i % 2 != 0] #(!= not equal to)
print("The odd numbers are:", odd_num)
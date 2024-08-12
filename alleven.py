numbers = [1, 33, 11, 44, 63, 16, 55, 5, 7, 14]

#sorting
numbers.sort()
print("The sorted list is:",numbers)

#to print all of the even numbers

even_num = [i for i in numbers if i % 2 == 0]
print("The even numbers are:", even_num)
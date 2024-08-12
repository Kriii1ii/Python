numbers = [1, 33, 11, 44, 63, 16, 55, 5, 7, 14]

#sorting
numbers.sort()
print("The sorted list is:",numbers)

#to print all of the prime numbers

def is_prime(n):
    if n<=1: #numbers less than or equal to 1 are not prime
        return False
    if n == 2:
        return True # 2 is a prime number
    if n % 2 == 0:
        return False #any even number greater than 2 is not prime
    i = 3 #next smallest old number 
    while i * i <= n: #checks the divisibiliuty upto the square root
        if n % i == 0: #if n is divisible by i it is not prime
            return False
        i += 2 #increases i by 2 each time (3+2, 5+2 jastai)
    return True
Prime_num = [i for i in numbers if is_prime(i)]
print("The prime numbers in the list are:", Prime_num)


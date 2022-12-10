# All Questions are from https://www.w3resource.com/c-programming-exercises/for-loop/index.php

# 1. Write a program in C to display the first 10 natural numbers. Go to the editor
# Expected Output :
# 1 2 3 4 5 6 7 8 9 10

# for i in range(1, 11):
#     print(i)

# 2. Write a C program to find the sum of first 10 natural numbers. Go to the editor
# Expected Output :
# The first 10 natural number is :
# 1 2 3 4 5 6 7 8 9 10
# The Sum is : 55


# sum = 0
# for i in range(1, 11):
#     sum = sum + i

# print("The Sum is: ", sum)


# perfeact number in 1 to 500

# for i in range(1, 500):
#     sum = 0
#     for j in range(1,int(i/2)):
#         if (i % j == 0):
#             sum = sum+j
#     if(sum == i):
#         print("  This is perfect number", i)

# gcd of a numbers

# a = int(input("a : "))
# b = int(input("b : "))
# i = 1

# while i<=a and i<=b:
#     if (a%i == 0 and b%i == 0):
#         gcd = i
#     i +=1
# print(gcd)

# Write a program in C++ to find the sum of digits of a given number

# number = int(input("Enter the number: "))
# sum = 0
# for i in range(number):
#     rem = number %10
#     number = int(number /10)
#     sum = sum + rem
# print(sum)

# Write a program in C++ to find the sum of the series 1 + 1/2^2 + 1/3^3 + ..+ 1/n^n

# number = int(input("Enter the number: "))
# sum = 0.0

# for i in range(1, number+1):
#     sum = sum + 1 / i**i


# print(sum)

# Write a program in C++ to calculate the series (1) + (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n).

# number = int(input("Enter the number: "))
# sum = 0
# totalSum = 0

# for i in range(1, number+1):
#     sum = sum + i
#     totalSum = totalSum+ sum

# print(totalSum)

# Write a program in C++ to calculate the sum of the series (1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n).

# number = int(input("Enter the number: "))
# sum = 0

# for i in range(1, number+1):
#     sum = sum + i*i

# print(sum)


# Write a program in C++ to find the sum of series 1 - X^2/2! + X^4/4!-.... upto nth term

# x = float(input("Enter the value for x: "))
# nTerm = int(input("Enter the value for nth Term: "))
# fact = 1.00
# sum = 1.00
# term = 1.00
# y = 2.00
# j = 1.0

# for i in range(1, nTerm+1):
#     fact = 1

#     for j in range(1, j < y+1):
#         fact = fact * j
#     term = term * (-1)
#     power = float(pow(x, y)/fact)
#     power = power*term
#     sum = sum + power
#     y += 2

# print(sum)

# Write a program in C++ to list non-prime numbers from 1 to an upperbound.

n = int(input("enter thr upper bound:"))
temp = None

for i in range(n+1):
    for j in range(2, i+1):
        if (n % i == 0):
            temp = i

    print(temp)

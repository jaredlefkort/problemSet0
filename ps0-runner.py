#Author: Jared Lefkort
#Date: 3/29/2016

import ps0

print("The number 4 is even: {}".format(ps0.is_even(4)))
print("The number 5 is even: {}".format(ps0.is_even(5)))


print("There are {} digits in the number 25".format(ps0.num_digits(25)))
print("There are {} digits in the number 100".format(ps0.num_digits(100)))

print("The sum of the digits in the number 15 is {}".format(ps0.sum_digits(15)))
print("The sum of the digits in the number 345 is {}".format(ps0.sum_digits(345)))
print("The sum of the digits in the number 9863 is {}".format(ps0.sum_digits(9863)))

print("The sum of the digits less then 3 is {}".format(ps0.sum_less_ints(3)))
print("The sum of the digits less then 6 is {}".format(ps0.sum_less_ints(6)))
print("The sum of the digits less then 50 is {}".format(ps0.sum_less_ints(50)))

print("The factorial of 3 is {}".format(ps0.factorial(3)))
print("The factorial of 10 is {}".format(ps0.factorial(10)))

print("2 is a factor of 10: {}".format(ps0.is_factor(10, 2)))
print("3 is a factor of 27: {}".format(ps0.is_factor(27, 3)))
print("5 is a factor of 625: {}".format(ps0.is_factor(625, 5)))
print("2 is a factor of 65: {}".format(ps0.is_factor(65, 2)))

print("4 is a prime number: {}".format(ps0.is_prime(4)))
print("11 is a prime number: {}".format(ps0.is_prime(11)))
print("25 is a prime number: {}".format(ps0.is_prime(25)))
print("31 is a prime number: {}".format(ps0.is_prime(31)))

print("6 is a perfect number: {}".format(ps0.is_perfect(6)))
print("28 is a perfect number: {}".format(ps0.is_perfect(28)))
print("30 is a perfect number: {}".format(ps0.is_perfect(30)))

print("6 divided by the number of digits has no remainder: {}".format(ps0.sum_divisible(6)))
print("16 divided by the number of digits has no remainder: {}".format(ps0.sum_divisible(16)))
print("20 divided by the number of digits has no remainder: {}".format(ps0.sum_divisible(20)))
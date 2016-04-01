#Author: Jared Lefkort
#Date: 3/29/2016


#-------------------------------Function 0-----------------------------------

def is_even(number):
	"""Takes a non-negative integer as a parameter
	returns True if the number is even
	returns False if the number is odd. """
	
	if number % 2 == 0: 
	#if there is no remainder the function will return true
		return True
	else:
		return False

#-------------------------------Function 1-----------------------------------

def num_digits(number):
	
	"""Takes a non negative integer as a parameter
	returns the number of digits in it"""
	incriment = 0
	
	while number > 0:
		number /= 10
		#gets rid of the last digit
		incriment += 1
	
	return incriment

#-------------------------------Function 2-----------------------------------

def sum_digits(digits):

	"""Takes a non negative integer as a parameter
	returns the sum of the digits"""
	
	sum = 0
	
	while digits > 0:
		finalNumber = digits % 10
		digits -= finalNumber 
		#this will get the last digit and then subtract it
		sum += finalNumber
		digits /= 10
	
	return sum

#-------------------------------Function 3-----------------------------------

def sum_less_ints(number):
	
	"""takes a non-negative integer as a parameter
	returns the sum of all of the integers that are less than the given number"""
	
	sum = 0
		
	while number > 0:
		number -= 1 
		#each time you go through the loop, the number will decrease by one, and then the new number will be added to the total
		sum += number
 
	return sum

#-------------------------------Function 4-----------------------------------

def factorial(number):

	"""takes a non-negative integer as a parameter
	returns its factorial"""
	
	product = 1
	
	while number > 0: 
	#each time you go through the loop, the product will be multiplied by the number, and then the number will be decreased, until the number reaches 0
		product *= number
		number -= 1
	
	return product

#-------------------------------Function 5-----------------------------------

def is_factor(number1, number2):

	"""Takes two positive integers as parameters
	figures out whether the second number is a factor of the first."""
	
	if number1 % number2 == 0:
	#if the remainder is 0, meaning that the second number is a factor of the first, the function will return true
		return True
	
	else:
		return False

#-------------------------------Function 6-----------------------------------

def is_prime(number):
	
	"""Takes an integer greater than or equal to 2 as a parameter
	Returns true if the number is prime, and false if the number is not."""
	
	divisor = 2
	
	while divisor < number:
	#the divisor will increase until it reaches the number.  
	#if the number is not prime, the loop will stop when it gets a remainder of 0
	#else it will continue until it reaches the number at which point it will return true
		if number % divisor == 0:
			return False
		divisor += 1

	else:
		return True
		
#-------------------------------Function 7-----------------------------------

def is_perfect(number):
	"""Takes a positive integer as a parameter.
	Returns True if the number is perfect and False if it is not."""
	
	sum = 0
	
	for numbers in range(1, number):
	#you need a range because you need to test the numbers less, to find the factors
		if number % numbers == 0:
		#when it finds that the number is a factor, it will add it to the total
			sum += numbers
	
	if sum == number:
	#at the end, if the sum equals the number then you know that it is a perfect number
		return True
	else:
		return False
			
	
	

#-------------------------------Function 8-----------------------------------

def sum_divisible(number):

	"""Takes a positive integer as a parameter. 
	Returns true if the sum of the digits of the number divide evenly into the number.
	Returns false if the sum of the digits of the number do not divide evenly into the number."""
	
	if number % sum_digits(number) == 0:
	#this will test if the number divided by the sum of its digits has no remainder, meaning that it is a factor, and will return true if it is true
		return True
	else:
		return False

#Author: Jared Lefkort
#Date: 3/29/2016


#-------------------------------Function 0-----------------------------------

def is_even(number):
	"""Takes a non-negative integer as a parameter
	returns True if the number is even
	returns False if the number is odd. """
	
	if number % 2 == 0:
		return True
	else:
		return False

#-------------------------------Function 1-----------------------------------

def num_digits(number):
	
	"""Takes a non negative integer as a parameter
	returns the number of digits in it"""
	incriment = 0
	
	for characters in number:
		incriment += 1
	
	return incriment

#-------------------------------Function 2-----------------------------------

def sum_digits(digits):

	"""Takes a non negative integer as a parameter
	returns the sum of the digits"""
	
	sum = 0
	
	for digit in number:
		sum = sum + int(digit)
	
	return sum

#-------------------------------Function 3-----------------------------------

def sum_less_ints(number):
	
	"""takes a non-negative integer as a parameter
	returns the sum of all of the integers that are less than the given number"""
	
	sum = 0
	
	for less_ints in number:
		number -= 1
		sum += number
	
	return sum

#-------------------------------Function 4-----------------------------------

def factorial(number):

	"""takes a non-negative integer as a parameter
	returns its factorial"""
	
	product = 0
	
	for less_ints in number:
		number -= 1
		product *= number
	
	return product

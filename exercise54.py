# This is where Exercise 5.4 goes
# Name:Ethan Puzarne


def is_triangle(x, y, z):
	'''is_triangle takes 3 integers and answers whether a 
	triangle can be formed with them. 

	print "no" when any one number is larger than the sum of the other two
	print "yes" otherwise'''

	if ((x > y + z) or (y > x + z) or (z > x + y)):
		print("no")
	else:
		print("yes")

is_triangle(1,2,3)
is_triangle(10,15,20)
is_triangle(100,100,300)


def user_triangle():
	'''Asks user for 3 integers and returns whether they make a triangle'''
	while True:
		try:
			x = int(raw_input("Please enter the first of three integers:"))
		except ValueError:
			print("Not an integer!")
			continue
		else:
			break
	while True:
		try:
			y = int(raw_input("Please enter the second of three integers: "))
		except ValueError:
			print("Not an integer!")
			continue
		else:
			break
	while True:
		try:
			z = int(raw_input("Please enter the third of three integers: "))
		except ValueError:
			print("Not an integer!")
			continue
		else:
			break
		
		
	is_triangle(x,y,z)

user_triangle()

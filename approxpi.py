"""Project 2.2: Approximating Pi
	Author: Danny Harris
	Description: This project aims to approximate the value of pi
	using the Monte Carlo algorithm, as well as graphically represent 
	data using turtle graphics.
	"""
import math
import random
import turtle

def isInCircle_stub(x, y, r):
        """(num, num, num)

	This function will determine whether or not the coordinates (x, y) for 
	the dart thrown has landed within the circle with radius (r), and 
	if it is, it will return True, otherwise, it will return False.

	>>>isInCircle(0, 0, 1)
	True
	>>>isInCircle(.5, .5, 1)
	True
	>>>isInCircle(1, 2, 1)
	False
	"""
        pass
        return #True or False

def montePi_stub(numDarts):
        """(num) -> float

	This function will take the input number (numDarts) as the number of times
	that pi should be approximated, and will return an approximate value for pi
	generated using the random module and will take those random values and will
	use the isInCircle function to determine if the coordinates lie within the 
	boundaries of the circle or not. A floating point number approximation of pi 
	will be returned.

	Note: The approximated values for pi will vary within each given input as the
	random coordinates will cause slight deviation in value returned.(i.e. An input
	of 100 could result in an approximated value of 3.08, 3.0, 2.88, etc.)

	>>>montePi(100)
	3.08
	>>>montePi(100000)
	3.143072
	"""
        pass
        return #float(approx)


def isInCircle(x, y, r):
	"""(num, num, num)

	This function will determine whether or not the coordinates (x, y) for 
	the dart thrown has landed within the circle with radius (r), and 
	if it is, it will return True, otherwise, it will return False.

	>>>isInCircle(0, 0, 1)
	True
	>>>isInCircle(.5, .5, 1)
	True
	>>>isInCircle(1, 2, 1)
	False
	"""
	hypo = math.sqrt(x**2 + y**2)
	if hypo <= r:
		return True
	else:
		return False

def montePi(numDarts):
	"""(num) -> float

	This function will take the input number (numDarts) as the number of times
	that pi should be approximated, and will return an approximate value for pi
	generated using the random module and will take those random values and will
	use the isInCircle function to determine if the coordinates lie within the 
	boundaries of the circle or not. A floating point number approximation of pi 
	will be returned.

	Note: The approximated values for pi will vary within each given input as the
	random coordinates will cause slight deviation in value returned.(i.e. An input
	of 100 could result in an approximated value of 3.08, 3.0, 2.88, etc.)

	>>>montePi(100)
	3.08
	>>>montePi(100000)
	3.143072
	"""
	counter = 0

	for i in range(numDarts):
		x = random.random()
		y = random.random()

		if isInCircle(x, y, 1) == True:
			counter += 1

	approx = counter/numDarts * 4

	return float(approx)

def showMontePi(numDarts):
	"""(num) -> turtle graphics + string

	This function will run nearly the same as the montePi function; however,
	this function will use turtle graphics to represent the positive coordinates
	(x, y) of darts thrown (numDarts) graphically such that the darts that land
	within the circle will appear as a blue dot, whereas the darts that land
	without the circle will appear as a red dot. The function, after all of the
	darts have been "thrown", will print a string given in the format seen below
	in the examples, in which it will include the number of iterations (numDarts),
	approximation for pi (approx), the math library value for pi, as well as the
	percent error (error) of the approximation, and lastly, the approximated value
	for pi (approx).

	Note: The approximated values for pi will vary within each given input as the
	random coordinates will cause slight deviation in value returned.(i.e. An input
	of 100 could result in an approximated value of 3.08, 3.0, 2.88, etc.)

	>>>showMontePi(100)
	With 100 iterations (dart):
	My approximate value for pi is: 3.08
	Math library pi value is 3.1415926535897932384626433832
	This is a 1.96 percent error.
	3.08
	>>>showMontePi(100000)
	With 100000 iterations (darts):
	My approximate value for pi is: 3.143072
	That is a 0.148 percent error.
	3.143072
	"""
	turtle.speed(0)
	turtle.Screen().setworldcoordinates(-2, -2, 2, 2)
	turtle.up()
	turtle.goto(-1, 0)
	turtle.down()
	turtle.goto(1, 0)

	turtle.up()
	turtle.goto(0, 1)
	turtle.down()
	turtle.goto(0, -1)

	counter = 0
	turtle.up()
	turtle.hideturtle()

	for i in range(numDarts):
		x = random.random()
		y = random.random()

		turtle.goto(x, y)

		if isInCircle(x, y, 1) == True:
			counter += 1
			turtle.color("blue")
		else:
			turtle.color("orange")

		turtle.dot()

	approx = counter/numDarts * 4

	turtle.Screen().exitonclick()

	error = round((abs(math.pi - approx)/math.pi)*100, 2)

	print("With " + str(numDarts) + " iterations (darts): \nMy approximate value for pi is: " + str(float(approx)) + "\nMath library pi value is: "
		+ str(math.pi) + "\nThis is a " + str(error) + " percent error. \n" + str(float(approx)))

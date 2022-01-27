"""Project 5.1: Zip Code to Barcode
	Author: Danny Harris
	Description: This project will take a
	5 digit zip code and convert this string
	to a Barcode using turtle graphics.
	
	"""
import turtle

def checkDigit(zip):
	"""(str) -> str
        This function takes a string value of a
        5 digit zip code, and converts each character
        to an integer, then adds it to variable total.
        Returns the check digit converted back to a
        string.

        >>> checkDigit("97403")
        '7'
        >>> checkDigit("92078")
        '4'
	"""
	total = 0
	for i in range(len(zip)):
		total += int(zip[i])
	remain = total % 10
	digit = 10 - remain
	return str(digit)

def drawZero():
	turtle.left(90)
	turtle.forward(50)
	turtle.up()
	turtle.backward(50)
	turtle.right(90)
	turtle.forward(10)
	turtle.pd()
	return None

def drawOne():
	turtle.left(90)
	turtle.forward(100)
	turtle.up()
	turtle.backward(100)
	turtle.right(90)
	turtle.forward(10)
	turtle.pd()
	return None

def zipToBar(zip):
	"""(str) -> None
        Takes a string parameter of a 5 digit zip code
        adds the check digit and converts the whole string
        to a barcode representation (with guard rails) using
        turtle graphics.
        Returns None.

        >>> zipToBar("97403")

        >>> zipToBar("92078")
        
	"""
	zip = zip + checkDigit(zip)
	binary = {"0": "11000", "1": "00011", "2": "00101", "3": "00110", 
	"4": "01001", "5": "01010", "6": "01100", "7": "10001", "8": "10010", 
	"9": "10100"}
	turtle.speed(0)
	drawOne()
	for i in range(len(zip)):
		barcode = binary.get(zip[i])
		for num in range(len(barcode)):
			if barcode[num] == "0":
				drawZero()
			else:
				drawOne()
	drawOne()
	return None

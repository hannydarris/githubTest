"""Project 2.1: Artshow
	Author: Danny Harris
	Description: This project will use turtle
	graphics to create an art show on the 
	turtle graphics canvas.
	"""
from turtle import *

def art_show_stub(art, length, pedals):
	"""(str, num, num) -> turtle graphics

	This function will take in parameters for the color of the line (art),
	the length of the sides of each octogon drawn (length), as well as the 
	number of pedals on the flower (pedals). It will print a flower on the
	canvas. Function returns none.

	>>>art_show_stub("green", 100, 60)
	None
	(will print out a green flower on the canvas.)
"""
	pass
	return #None


def drawOctogon(line):
	"""(num) -> turtle graphics

	This function will take in the parameter (line) and will use that 
	length for each side of an octogon which will be drawn using 
	turtle graphics and a for loop and will print an octogon on the canvas.
"""
	for i in range(8):
		fd(line)
		left(45)

def art_show(art, length, pedals):
	"""(str, num, num) -> turtle graphics

	This function will use turtle graphics and the pre-existing
	drawOctogon function in combination with a for loop to create
	an art show of in which the final product will be a flower. 
	The function will take in the parameters for color, length of 
	each side of an octogon, and the number of times an octogon will 
	be drawn, thus creating a flower. Function will return none.

	>>>art_show("red", 150, 90)
	None
	(This function will draw a red flower on the canvas.)
"""
	speed(0)
	color(art)
	for i in range(pedals):
		drawOctogon(length)
		left(360/pedals)

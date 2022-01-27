"""Project 3.2: Memorable PINs
	Author: Danny Harris
	Description: This project will have a function alphapinEncode
	which will take an integer (pin) and will return a coded pin
	in string format.
	"""

import doctest

def alphapinEncode_stub(pin):
	"""(int) -> str

        This function will take an integer (pin), and will return
        a string representation of those numbers (phonic).

        >>> alphapinEncode(4327)
        'lohi'
        >>> alphapinEncode(1298)
        'dizo'
	"""
	pass
	return #phonic

def alphapinEncode(pin):
	"""(int) -> str

        This function will take an integer (pin), and will return
        a string representation of those numbers (phonic). The
        function will run while the pin is greater than 0, and
        the last two digits of the pin will be removed with each
        iteration until the pin runs out of digits. Within each
        iteration, the two digits removed will first be converted
        to a corresponding vowel and consonant using indeces, and
        that combination of two letters will be added to the beginning
        of phonic. After all iterations have run, phonic will be
        returned.

        >>> alphapinEncode(4327)
        'lohi'
        >>> alphapinEncode(1298)
        'dizo'
	"""
	vowels = "aeiou"
	consonants = "bcdfghjklmnpqrstvwyz"
	phonic = ""
	while pin > 0:
		tens = pin%100
		vIndex = tens%5
		cIndex = tens//5
		sound = consonants[cIndex] + vowels[vIndex]
		phonic = sound + phonic
		pin = pin//100
	return phonic

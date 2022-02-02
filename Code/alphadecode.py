"""Project 4: AlphaPin Decode
	Author: Danny Harris
	Description: This project will decode a string parameter
	(tone) into an integer (decode) which will be the numerical
	representation of the encoding done in project 3.2.

	"""
import doctest

def alphapinDecode(tone):
	"""(str) -> integer

	Converts a string variable (tone) encoding back to the integer
	representation (decode), virtually undoing the encoding done 
	in project 3.2.
	If the parameter is an empty string, function will print an 
	error message and return None.

	>>> alphapinDecode("lohi")
	4327
	>>> alphapinDecode("dizo")
	1298
	>>> alphapinDecode("bomejusa")
	3463470
	>>> alphapinDecode("bomelela")
	3464140
	>>> alphapinDecode("")
	Tone is not in correct format.
	"""
	vowels = "aeiou"
	consonants = "bcdfghjklmnpqrstvwyz"
	decode = ""
	if len(tone) == 0:
		print("Tone is not in correct format.")
		return None
	else:
		for i in range(len(tone)):
			if tone[i] in consonants:
				cNum = consonants.index(tone[i])*5
				vNum = vowels.index(tone[i+1])
				pairNum = cNum + vNum
				decode += str(pairNum)
		return int(decode)
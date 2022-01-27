""" Project 0: Temperature Conversion
	Author: Danny Harris
	Description: This project aims to convert Celsius temperature to Farenheit temperature,
	using the ctemp_to_ftemp function with parameter temp,
	and will return the resulting Farenheit temperature.
	"""

def ctemp_to_ftemp_stub(temp):
	"""
	(number) -> float

	Converts Celsius temperature, temp, to Farenheit temperature, ftemp,
	then returns the Farenheit temperature, ftemp.

	>>>ctemp_to_ftemp(30)
	86.0
	>>>ctemp_to_ftemp(21.1)
	69.98
	"""
	pass
	return #float(ftemp)


def ctemp_to_ftemp(temp):
	"""
	(number) -> float

	Converts Celsius temperature, temp, to Farenheit temperature, ftemp,
	then returns the Farenheit temperature, ftemp.

	>>> ctemp_to_ftemp(30)
	86.0
	>>> ctemp_to_ftemp(21.1)
	69.98
	"""
	ftemp = (9/5)*temp + 32
	return float(ftemp)

print(ctemp_to_ftemp(30))
print(ctemp_to_ftemp(21.1))

"""Project 5.2: String Reversal
	Author: Danny Harris
	Description: This project will go about reversing
	a string using two different approaches. The first,
	strReverseI() will use iteration to reverse a string
	while the second, strReverseR() will use recursion to
	reverse the string.
	"""
import doctest
def strReverseI(s):
	"""(str) -> str
        This function will use iteration to reverse
        the string parameter s.
        This function is iterative because it uses
        a for loop.
        String variable reverse will be returned.

        >>> strReverseI("CIS 210")
        '012 SIC'
        >>> strReverseI("")
        ''
	"""
	reverse = ""
	for i in range(len(s)):
		reverse = s[i] + reverse
	return reverse

def strReverseR(s):
	"""(str) -> str
        This function will use recursion to reverse
        the string parameter s.
        This function is recursive because it calls
        itself.
        String variable reverse will be returned.

        >>> strReverseR("CIS 210")
        '012 SIC'
        >>> strReverseR("")
        ''
	"""
	reverse = ""
	if len(s) == 0:
		return reverse
	else:
		reverse = s[-1:] + strReverseR(s[:-1])
		return reverse

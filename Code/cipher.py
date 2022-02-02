"""	Project 3.1: Substitution Cipher
	Author: Danny Harris
	Description: This project aims to encrypt a string (plainText)
	as well as decrypt the returned cipherText by using the two main 
	functions substitutionEncrypt and substitutionDecrypt. These functions
	will call another function genKey which will create a key to map the 
	encryption of the plainText and the decryption of the cipherText. This
	function will call the functions removeDupes and removeMatches in order
	to create a key from a given password and the alphabet.
"""
import doctest

def removeDupes(password):
	"""(str) -> str

	This function will take in a single-word parameter (password), 
	and will return that same word with all duplicate letters removed.
	By taking the password and iterating through each letter in the 
	string, the function will append each letter to an empty variable
	(newPass) once, such that no letter can be added more than once.

	>>> removeDupes("messages")
	'mesag'
	"""
	newPass = ""
	for ch in password:
		if ch not in newPass:
			newPass = newPass + ch
	return newPass

def removeMatches(alpha, passw):
	"""(str, str) -> str

	This function will take the password (passw), and search for 
	the occurrences of each letter of passw in an alphabet (alpha).
	Then will return alpha with all letters of passw removed from 
	the string.

	>>> removeMatches("abcdefghijklmnopqrstuvwxyz", "word")
	'abcefghijklmnpqstuvxyz'
	"""
	newKey = ""
	for ch in alpha:
		if ch not in passw:
			newKey = newKey + ch
	return newKey

def genKey(password):
	"""(str) -> str

	This function will call on the removeDupes function as well as 
	the removeMatches function. Taking in a parameter (password), and
	removing duplicate letters from that string using the removeDupes
	function, it will then remove those letters from the key and will
	split up the key into two parts, one part consists of all the letters
	in the key that occur after the last letter in the password (afterPassword),
	and the other will consist of all the letters before the last letter 
	in the password (beforePassword).
	Then, these pieces will be reassigned to the value of the key such that
	the beginning of the key is the password with duplicate letters removed,
	followed by afterPassword and then beforePassword.

	>>> genKey("ajax")
	'ajxyzbcdefghiklmnopqrstuvw'
	"""
	key = "abcdefghijklmnopqrstuvwxyz"
	password = removeDupes(password)
	lastChar = password[-1]
	nextChar = key.find(lastChar)
	afterPassword = removeMatches(key[nextChar+1:], password)
	beforePassword = removeMatches(key[:nextChar], password)
	key = password + afterPassword + beforePassword
	return key

def substitutionEncrypt(plainText, password):
	"""(str, str) -> str

	This function takes the string (plainText) and a password (password)
	as parameters, and returns an encrypted version of the plainText. 
	Before the encryption process begins, the plainText parameter will have 
	all spaces removed between words and will be converted to lower case.
	By mapping indeces, or letters, of the plainText found in the alphabet, to 
	indeces in the key (generated from the password), an encrypted version of the 
	plainText (cipherText) will be returned.

	>>> substitutionEncrypt("the quick brown fox", "ajax")
	'qdznrexgjoltkblu'
	"""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	key = genKey(password)
	cipherText = ""
	plainText = plainText.replace(" ", "").lower()
	for i in range(len(plainText)):
		index = plainText[i]
		loc = alphabet.find(index)
		cipherText = cipherText + key[loc]
	return cipherText

def substitutionDecrypt(cipherText, password):
	"""(str, str) -> str

	This function takes the encrypted text (cipherText), as well as 
	a password (password), and will use the password to generate the 
	key needed to decrypt the cipherText. This function will map the 
	indeces, or letters of the cipherText found in the key to matching 
	indeces in the alphabet in order to decrypt the cipherText. The 
	decrypted text will be returned.
	Note: Since the spaces were removed in the Encryption function, spaces
	will not need to be removed from the cipherText in this function.

	>>> substitutionDecrypt("qdznrexgjoltkblu", "ajax")
	'thequickbrownfox'
	"""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	key = genKey(password)
	plainText = ""
	for i in range(len(cipherText)):
		idx = cipherText[i]
		local = key.find(idx)
		plainText = plainText + alphabet[local]
	return plainText

def substitutionDecrypt_stub(cipherText, password):
    """(str, str) -> str

    This function will take the cipherText input generated from the
    substitutionEncrypt function, as well as the password used in the
    substitutionEncrypt function, and will return the decrypted (plainText)
    version of the sentence.

    >>> substitutionDecrypt("qdznrexgjoltkblu", "ajax")
    'thequickbrownfox'
    """
    pass
    return #plainText


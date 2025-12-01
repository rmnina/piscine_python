import sys

def countChar(object=None) -> None:
	"""
	Provides data about the text passed as an argument.

	Counts :
		- the total number of characters
		- the number of upper letters
		- the number of lower letters
		- the number of punctuation symbols
		- the number of spaces
		- the number of digits

	Takes a str as a parameter, asks user for input if
	nothing is provided.

	Does not return any value, prints the data in the 
	terminal.
	"""

	none = 0
	
	try:
		if object is None:
			object = input('What is the text to count?\n')
			none = 1
		assert isinstance(object, str), "Argument is not a string"
	except EOFError:
		print("No input recieved (EOF)")
		return
	except AssertionError as error:
		print(f"Assertion error: {error}")
		return

	if none == 1:
		object += '\n'

	upper, lower, punct, spaces, digits = 0, 0, 0, 0, 0

	punctList = r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

	for x in object:
		if x.isdigit():
			digits += 1
		elif x.isupper():
			upper += 1
		elif x.islower():
			lower += 1
		elif x.isspace():
			spaces += 1
		elif x in punctList:
			punct += 1

	print(f"The text contains {len(object)} characters:")
	print(f"{upper} upper letters")
	print(f"{lower} lower letters")
	print(f"{punct} punctuation marks")
	print(f"{spaces} spaces")
	print(f"{digits} digits")


def main():
	args = sys.argv

	try:
		assert len(args) < 3, "Only one argument is expected"
	except AssertionError as error:
		print(f"AssertionError: {error}")
		return

	countChar(args[1] if len(args) == 2 else None)
	return 0

if __name__ == "__main__":
	main()
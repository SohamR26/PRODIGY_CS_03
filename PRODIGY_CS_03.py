def password(user_input):

	n = len(user_input)

	hasLower = False
	hasUpper = False
	hasDigit = False
	specialChar = False
	normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

	for i in range(n):
		if user_input[i].islower():
			hasLower = True
		if user_input[i].isupper():
			hasUpper = True
		if user_input[i].isdigit():
			hasDigit = True
		if user_input[i] not in normalChars:
			specialChar = True


	print("Strength of password:-", end = "")
	if (hasLower and hasUpper and hasDigit and specialChar and n >= 8):
		print("Strong")

	elif ((hasLower or hasUpper) and specialChar and n >= 6):
		print("Moderate")
	else:
		print("Weak")


if __name__=="__main__":

	user_input = input("Enter the password :-")

password(user_input)
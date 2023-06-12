from parameters import UserInput


def ifPrint(text):
	if UserInput.printFlag.value:
		print(text)
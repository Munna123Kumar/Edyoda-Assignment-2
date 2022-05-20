# Python3 program to check if a string contains any special character

import re

def run(string):
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	if(regex.search(string) == None):
		print("String is accepted")
		
	else:
		print("String is not accepted.")
if __name__ == '__main__' :
	
	# Enter the string
	string = "Python@is a&high level*programming language"
	
	# calling run function
	run(string)

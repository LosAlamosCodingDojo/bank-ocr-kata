#! /usr/bin/env python

#A pseudo-OCR reader.  Takes in a file with account numbers in a 7-segment display format,
#and prints out the account numbers in ASCII text.  It also checksums the accounts, and 
#attempts to fix errors if possible.

#by Scot Halverson

import sys

# a dict to map a binary representation of the 7 segments into the digit it represents
binDigits = {119:0, 36:1, 18:1, 93:2, 109:3, 46:4, 107:5, 122:6, 123:6, 37:7, 127:8, 111:9}

#print the binary 7 segment number
def printBin(binDigit):
	#basically, we're just setting characters in a 3x3 char array based on powers of 2
	lines = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
	lines[0][1] = '_' if (binDigit & 1) > 0 else ' '
	lines[1][0] = '|' if (binDigit & 2) > 0 else ' '
	lines[1][2] = '|' if (binDigit & 4) > 0 else ' '
	lines[1][1] = '_' if (binDigit & 8) > 0 else ' '
	lines[2][0] = '|' if (binDigit & 16) > 0 else ' '
	lines[2][2] = '|' if (binDigit & 32) > 0 else ' '
	lines[2][1] = '_' if (binDigit & 64) > 0 else ' '

	print "".join(lines[0])
	print "".join(lines[1])
	print "".join(lines[2])
	print "\n"
	return 0

#small function to take an account in 7 segment binary into a decimal string
def binToString(acct):
	result = ''
	for v in acct:
		try:	#try to look up the 7 segment binary in digit map
			result += str(binDigits[v])	#great success
		except:
			result +='?'			#not found
	return result

#parse a 3x3 char array (7 segment display) into its binary representation
def parseDigit(lines):
	#the opposite of the print function... check various characters in 3x3 char array
	#and add powers of 2 based on what's found
	digit = 0
	digit += 1 if lines[0][1] == '_' else 0
	digit += 2 if lines[1][0] == '|' else 0
	digit += 4 if lines[1][2] == '|' else 0
	digit += 8 if lines[1][1] == '_' else 0
	digit += 16 if lines[2][0] == '|' else 0
	digit += 32 if lines[2][2] == '|' else 0
	digit += 64 if lines[2][1] == '_' else 0

	return digit

#This function takes in a 7 segment binary digit and produces a list of valid digits produced
#by a 1 segment modification
def segmentMod(digit):
	possibilities = []	#create list of possibilities
	for i in xrange(7):	#iterate through 0-6, for segment ids
		#if the digit has segment i on, and we remove it, is that valid?
		if digit & (2**i) > 0 and (digit - (2**i)) in binDigits:
			possibilities.append(digit - (2**i))	#add the possibility
		#if the digit has segment i off, and we add it, is that valid?
		elif digit & (2**i) == 0 and (digit + (2**i)) in binDigits:
			possibilities.append(digit + (2**i))	#add the possibility
	return possibilities

#this function will generate a list of possible account #s generated by modifying 1 segment
#amongst the digits.  Note that this works for both malformed and checksum issues.  If it's 
#just a checksum issue, any digit can be modified.  If a digit is malformed, only 
#modifications to that digit could possibly result in a valid checksum.
def fixBad(acct):
	possibilities = []	#create array for possibilities
	for i,item in enumerate(acct):		#iterate through acct digits
		for dig in segmentMod(item):	#find 1 segment modifications producing digit
			temp = acct[:]		#copy acct
			temp[i] = dig		#replace digit with modification
			possibilities.append(binToString(temp))	#append full acct to possibilites
	return possibilities

#validation function - if there is something wrong with the acct number, this function
#calls the functions that fix it
def validate(acct):	 
	possibilities = []		#create an array for possibilities in case of problems
	string = binToString(acct)	#convert account to string
	problem = ''			#create a problem descriptor string
	if '?' in string:		#fix misread digits
		possibilities = fixBad(acct)	#get possible digit replacements
		problem = " ILL"		#set problem to ill-formed
	else:
		if checksum(string):	#valid checksum, we're done
			return string	
		else:			#otherwise, we've got a bad checksum
			possibilities = fixBad(acct)	#so we fix that too
			problem = " ERR"		#and set the problem to ERR
	validPossibilities = []		#create an array for valid possibilities (good cs)
	for p in possibilities:		#iterate through returned possibilities
		if checksum(p):		#run checksum
			validPossibilities.append(p)	#if valid, they go in valid possibilites
	if len(validPossibilities) == 0:	#then we check how many possibilities we have
		return string + problem		#if 0, return original string + problem
	if len(validPossibilities) == 1:	#if 1, just return the fixed acct
		return validPossibilities[0]	
	string += ' AMB ['			#otherwise, create a list of possibilities
	for p in validPossibilities:		#along with the original and a problem 
		string += p + ', '		#of AMB for ambiguous
	string = string[:-2] + ']'
	return string

#check that the string meets the checksum requirements.
#basic idea is sum( (9-i)*digit[i]) % 11 == 0 
def checksum(string):
	if '?' in string:	#check for misread characters
		return False
	sum = 0			#init sum
	i = 9			#start coeff at 9
	for v in list(string):	#iterate through digits
		if v.isdigit():	#make sure its actually a digit
			sum += (int(v) * i)	#if so, add coeff * digit to sum
		else:		#otherwise it fails
			return False
		i -= 1		#decrement coeff
	if (sum % 11) != 0:	#then check that its divisible by 11
		return False	
	return True

#take a set of 4 lines and parse it into the digits it represents
def parseAcct(lines):
	digit = ['']*3	#3 empty strings to hold the digit
	acct = []	#empty list for account digits in 7 segment binary 
	for i in range(len(lines[0])/3):	#iterate through the 3 lines 3 chars at a time 
		digit[0] = lines[0][i*3:(i+1)*3]	
		digit[1] = lines[1][i*3:(i+1)*3]
		digit[2] = lines[2][i*3:(i+1)*3]
		acct.append(parseDigit(digit))		#parse digit and append to acct
	return validate(acct)				#then validate

#read a file representing a set of account numbers in 7 segment display format
def parseFile():
	lines = ['']*4	#list of 4 empty strings
	accts = []	#list of accounts parsed
	with open(sys.argv[1]) as f:	#iterate through the lines in chunks of 4
		for count,line in enumerate(f):
			lines[count % 4] = line
			if count % 4 == 3:	#parse the account and add to accounts
				accts.append(parseAcct(lines))
	return accts

def main():
	#parse the file
	data = parseFile()
	#display the results
	for item in data:
		print item

#call the main function
if __name__ == '__main__':
	#check that the user provided an input file.  If not, show how to call program
	if len(sys.argv) < 2:
		print './OCR.py /path/to/input/file.txt'
		exit(-1)
	main()
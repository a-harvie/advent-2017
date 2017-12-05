import math

answer_input = 368078
test_inputs = ["abcde fghij","abcde xyz ecdab","a ab abc abd abf abj","iiii oiii ooii oooi oooo","oiii ioii iioi iiio"]

def testString(s):
	l = s.split()
	st = set()
	for i in l:
		st.add(''.join(sorted(i)))

	return len(st) == len(l)

def test():
	for i in test_inputs:
		print(testString(i))

def answer():
	c = 0;
	with open('04/04_input.txt') as f:
		for l in f:
			if testString(l):
				c += 1
		print(c)

test()
answer()
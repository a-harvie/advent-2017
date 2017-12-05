import math

answer_input = 368078
test_inputs = ["aa bb cc dd ee","aa bb cc dd aa","aa bb cc dd aaa"]

def testString(s):
	l = s.split()
	st = set()
	for i in l:
		st.add(i)

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
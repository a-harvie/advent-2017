test_inputs = [
"pbga (66)",
"xhth (57)",
"ebii (61)",
"havc (66)",
"ktlj (57)",
"fwft (72) -> ktlj, cntj, xhth",
"qoyq (66)",
"padx (45) -> pbga, havc, qoyq",
"tknk (41) -> ugml, padx, fwft",
"jptl (61)",
"ugml (68) -> gyxo, ebii, jptl",
"gyxo (61)",
"cntj (57)"
]

def line_parser(l):
	p = l.split(' -> ')
	p[0] = p[0].split(' ')
	p[0][1] = p[0][1][1:-1]
	if len(p) > 1:
		p[1] = p[1].split(', ')
	return p

def find_root(l):
	children = set()
	root = None
	for i in l:
		if len(i) > 1:
			for j in i[1]:
				children.add(j)

	# root will be element that has children but is not a child
	for i in l:
		if len(i) > 1 and i[0][0] not in children:
			root = i[0][0]

	return root

def test():
	items = []
	for i in test_inputs:
		items.append(line_parser(i))
		print(line_parser(i))
	
	find_root(items)

def answer():
	with open('07/07_input.txt') as f:
		items = []
		for ln in f:
			items.append(line_parser(ln.strip()))
		print(items)
		print(find_root(items))

test()
answer()
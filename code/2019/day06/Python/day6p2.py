with open("input.txt") as f:
	data = f.read().split()

data = [d.split(')') for d in data]

class Node:
	def __init__(self, name, children = None):
		self.name = name
		self.depth = 0
		if children is not None:
			self.children = children
		else:
			self.children = []

	def __repr__(self):
		return f"{self.name}"

	def query(self, q):
		if self.name == q:
			return self
		else:
			for c in self.children:
				qu = c.query(q)
				if qu != None:
					return qu
		return None


com = Node('COM')
heads = [com]
for d in data:
	#print(d)
	for h in heads:
		if h.name == d[0]:
			head = h
			break
	else:
		head = None
		for h in heads:
			head = h.query(d[0])
			if head is not None:
				break

		if head is None:
			head = Node(d[0])
			heads.append(head)

	for h in heads:
		if h.name == d[1]:
			tail = h
			heads.remove(h)
			break
	else:
		tail = Node(d[1])

	head.children += [tail]


def traverse(N, f, d=0):
	a = f(N,d)
	if N != None:
		for i in N.children:
			a += traverse(i, f, d+1)
	return a

def setDepth(N,d):
	N.depth = d
	return 0

def getDepth(N,d):
	return N.depth

traverse(com, setDepth)

def getParent(n, p=com):
	if isinstance(n, str):
		n = com.query(n)

	if n == com:
		return None

	if n in p.children:
		return p
	
	for c in p.children:
		s = getParent(n, c)
		if s is not None:
			return s
	return None


def transfer(cNode,dNode):
	if isinstance(cNode, str):
		cNode = com.query(cNode)
	if isinstance(dNode, str):
		dNode = com.query(dNode)

	if cNode == None or dNode == None:
		return -1

	chainC = []
	cP = cNode
	while (cP != com):
		cP = getParent(cP)
		chainC += [cP]

	chainD = []
	dP = dNode
	while (dP != com):
		dP = getParent(dP)
		chainD += [dP]
	joint = None
	for p in chainC:
		if p in chainD:
			joint = p
			break
	return cNode.depth + dNode.depth - (joint.depth*2)
output = transfer(getParent("YOU"),getParent("SAN"))
print(f"Part 2:{output}")

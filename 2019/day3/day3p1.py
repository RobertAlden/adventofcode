from statistics import median

with open("input.txt") as f:
	data = f.readlines()

data = [d.split(',') for d in data]
wires = []
for wire in data:
	new_wire = [(0,0,0)]
	px = 0
	py = 0
	mag = 0
	for w in wire:
		if w[0] == 'R':
			px += int(w[1:])
		elif w[0] == 'L':
			px += -int(w[1:])
		elif w[0] == 'U':
			py += int(w[1:])
		elif w[0] == 'D':
			py += -int(w[1:])
		mag += int(w[1:])
		new_wire.append((px,py,mag))
	wires.append(new_wire)

print(wires)

def intersection(seg1,seg2):
	s1p1 = seg1[0]
	s1p2 = seg1[1]
	s1mag = seg1[1][2]
	s2p1 = seg2[0]
	s2p2 = seg2[1]
	s2mag = seg2[1][2]
	s1dir = 0
	s2dir = 0
	if s1p1[0] == s1p2[0]:
		s1dir = 1
	else:
		s1dir = 0
	if s2p1[0] == s2p2[0]:
		s2dir = 1
	else:
		s2dir = 0
	if s1dir == s2dir:
		return [] # Parallel, no intersect
	else:
		if s1dir == 1:
			# seg1 is vertical
			if median([s1p1[0],s2p1[0],s2p2[0]]) == s1p1[0]:
				if median([s2p1[1],s1p1[1],s1p2[1]]) == s2p1[1]:
					i_mag = (s1mag-abs(s1p2[1]-s2p1[1])) + (s2mag-abs(s2p2[0]-s1p1[0]))
					return [(s1p1[0],s2p1[1],i_mag)]
			else:
				return []
		else:
			#seg1 is horizontal
			if median([s1p1[1],s2p1[1],s2p2[1]]) == s1p1[1]:
				if median([s2p1[0],s1p1[0],s1p2[0]]) == s2p1[0]:
					i_mag = (s1mag-abs(s1p2[0]-s2p1[0])) + (s2mag-abs(s2p2[1]-s1p1[1]))
					return [(s2p1[0],s1p1[1],i_mag)]
			else:
				return []

crosses = []
for i in range(len(wires[0])-1):
	segment1 = (wires[0][i],wires[0][i+1])
	for k in range(len(wires[1])-1):
		segment2 = (wires[1][k],wires[1][k+1])
		test = intersection(segment1,segment2)
		if test != None:
			crosses += (test)

crosses = [(abs(i[0])+abs(i[1]),i[2]) for i in crosses]

print(sorted(crosses,key=lambda x:x[1]))
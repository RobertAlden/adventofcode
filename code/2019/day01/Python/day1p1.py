data = []
with open("input.txt") as f:
	data = [int(i) for i in f]

output = sum([int(x/3)-2 for x in data])
print(output)
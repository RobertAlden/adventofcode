data = []
with open("input.txt") as f:
	data = [int(i) for i in f]



def fuel_needed(n):
	total = 0
	current = n
	while (int(current / 3) - 2 > 0):
		current = int(current / 3) - 2
		total += current
	return total

output = sum([fuel_needed(x) for x in data])
print(output)
with open("test.txt") as f:
	data = f.read().split()

data = [d.split(')') for d in data]
print(data)
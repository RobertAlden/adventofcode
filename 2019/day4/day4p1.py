start = 367479
end = 893698

def increases(n):
	digits = [int(i) for i in list(str(n))]
	delta = 0
	digits = [digits[i + 1] - digits[i] for i in range(len(digits) - 1)]
	for i in digits:
		if i < 0:
			return False
	return True

def doubled(n):
	digits = [int(i) for i in list(str(n))]
	digits = [digits[i + 1] == digits[i] for i in range(len(digits) - 1)]
	if len([i for i in digits if i]) > 0:
		return True
	return False

def validate(n):
	if increases(n) and doubled(n):
		if start < n < end:
			return True
	return False

count = 0
for i in range(start,end):
	if validate(i):
		print(i)
		count += 1

print(count)
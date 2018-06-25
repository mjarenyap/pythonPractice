def fizzbuzz(x, a, b):
	result = ""
	if(x % a == 0):
		result += "Fizz"

	if(x % b == 0):
		result += "Buzz"

	if(len(result) == 0):
		result = str(x);

	print(result)

n = int(input("Type n: "))
a = int(input("Type a: "))
b = int(input("Type b: "))

for x in range(n):
	fizzbuzz(x+1, a, b)
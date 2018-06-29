def blackjack(a, b):
	if(a == 11):
		a = 1

	if(b == 11):
		b = 1

	result = a + b
	if(result > 21):
		return 0

	else:
		return result

print("Type 2 numbers: ")
a = int(input(""))
b = int(input(""))
print(blackjack(a, b))
def convert(x, currency):
	converted = 0.00
	if(currency == "POUNDS"):
		converted = x * 0.84

	elif(currency == "LIRA"):
		converted = x * 2040

	elif(currency == "FRANCS"):
		converted = x * 9.85

	elif(currency == "MARKS"):
		converted = x * 3.23

	else:
		converted = x * 260

	print("$",x," CONVERTS TO ",converted," ",currency)

# main driver
n = int(input(""))
inputs = []
for i in range(n):
	inputs.append(input())

for curr in inputs:
	stmnt = curr.split(" ")
	convert(float(stmnt[0]), stmnt[1])
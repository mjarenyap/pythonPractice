def who_wins(a, b):
	if(a == "R" and b == "S"):
		print("A Wins")
		return 1

	elif(a == "S" and b == "P"):
		print("A Wins")
		return 1

	elif(a == "P" and b == "R"):
		print("A Wins")
		return 1

	elif(a == b):
		print("DRAW")
		return 0

	else:
		print("B Wins")
		return 0

rounds = int(input())
comps = input()
player_1 = 0

for i in range(rounds):
	next_round = comps[:2] # gets the first two letters
	player_1 += who_wins(next_round[0]+"", next_round[1]+"")
	comps = comps[2:] # removes the first two letters

if(player_1 >= rounds / 2 and rounds % 2 == 1):
	print("A Wins Tournament")

elif(player_1 > rounds / 2 and rounds % 2 == 0):
	print("A Wins Tournamet")

elif(player_1 == rounds / 2 and rounds % 2 == 0):
	print("DRAW")

else:
	print("B Wins Tournament")

import random
words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

guesses = ''
turns = 12
while turns > 0:
	failed = 0
	for char in word:
		if char in guesses:
			print(char, end=" ")

		else:		
			print("____")
			failed += 1

	if failed == 0:
		print("You Win")
		print("The word is: ", word)
		break
	print()
	guess = input("guess a character:")

	guesses += guess

	if guess not in word:
		turns -= 1
		print("Wrong")
		print("You have", + turns, 'more guesses')
		print("The word is: ", word)
		

		if turns == 0:
			print("You Loose")

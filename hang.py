word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")

for i in range(45):
	print()

# Some useful variables
guesses = []
maxfails = 8
wordtoGuess = []

for letter in word:
	wordtoGuess.append("_")
print("word to guess:", wordtoGuess)

maxfails -= 1
while maxfails != 0:
	guess = input("Guess a letter: ")
	if guess in guesses:
		print("You already guessed this. Guess again!")
	elif guess in word:
		for i in range(len(word)):
			if word[i]==guess:
				wordtoGuess[i] = guess
				print("Word to guess:", wordtoGuess)
		if "_" not in wordtoGuess:
			print("Congrats! You win!")
			break
	elif guess not in word:
		guesses.append(guess)
		maxfails -= 1
		print("Not in word. Tries remaining: ", maxfails)
if maxfails == 0:
	print("The correct word was", word)

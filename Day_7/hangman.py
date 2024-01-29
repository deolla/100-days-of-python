import random 

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = ['_' for _ in range(len(chosen_word))]

guess = input("Guess a letter: ").lower()


for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display[i] = guess
print(display)

for i in chosen_word:
    if i == guess:
        print("Right")
    else:
        print("Wrong")

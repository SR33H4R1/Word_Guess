import random

# Word guessing game

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'water']

chance = 12

name = input("Enter your name : ")
print(f"Hello {name}. Best of luck!!!")

word = random.choice(words)

turn = 1
guesses = []
print(word)

while turn < chance:
    if len(guesses) == len(word):
        break
    else:
        print(f"You have {chance - turn} chances.")
        print("\nGuess a letter !!!")
        for x in range(len(word)):
            if x in guesses:
                print(word[x])
            else:
                print("_")

        t = input("\nEnter your guess : ")

        if t in word:
            y = word
            i = word.index(t)

            if i in guesses:

                y = word[:i] + word[i + 1:]

                guesses.append(y.index(t) + 1)
            else:

                guesses.append(word.index(t))

            print(f"\nYou guessed right.")

        else:
            print(f"\nYou guessed wrong.")
            turn += 1

if len(guesses) == len(word):
    print(f"\nHurray you have won. The word is {word}")
else:
    print(f"\nYou have wasted your chances . The word was {word}")

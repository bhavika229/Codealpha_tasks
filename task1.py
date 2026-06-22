import random

words = ["apple", "banana", "grape", "orange", "peach"]
word = random.choice(words)
guesses = []
attempts = 6

while attempts > 0:
    display = [letter if letter in guesses else "_" for letter in word]
    print("Word: " + " ".join(display))

    if "_" not in display:
        print("🎉 You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print("Already guessed!")
        continue

    guesses.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"Wrong! {attempts} guesses left.")

else:
    print(f"😢 You lost! The word was '{word}'.")

import random

words = ["apple", "table", "chair", "house", "snake"]
         
word = random.choice(words)


guessed = ["_"] * len(word)
attempts = 6
print(" Welcome to Hangman!")
print("Guess the word:", " ".join(guessed))
while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.")
        continue

    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

    
    print("Word:", " ".join(guessed))


if "_" not in guessed:
    print("🎉 You win! The word was:", word)
else:
    print("💀 You lose! The word was:", word)

import random

def choose_random_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    secret_word = choose_random_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    
    while True:
        print("\nAttempts left:", attempts_left)
        print(display_word(secret_word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            if all(letter in guessed_letters for letter in secret_word):
                print("\nCongratulations! You guessed the word:", secret_word)
                break
        else:
            attempts_left -= 1
            if attempts_left == 0:
                print("\nGame over! The word was:", secret_word)
                break

def main():
    hangman()

if __name__ == "__main__":
    main()

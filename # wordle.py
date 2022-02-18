# wordle
# eric johnson
# feb 17, 2022

todays_word = "shake"
word_list = ["shape, shake, shale, shame, shave, shade"]

# Creating header to increase terminals readability
def game_intro():
    print("\n" * 10)
    print("#" * 50 + "\n" + "#" * 50)
    print("\nWelcome to my version of Wordle!")
    print("\nQuick Tip:")
    print("[O] = Correct letter in correct position")
    print("[X] = Letter is in word, but wrong position\n")
    print("#" * 50 + "\n" + "#" * 50)
    print("\n")

# Checks users guess against the days solution, prints "map" of guesses
def check_letters(word, solution):
    letter_check = []
    for x in range(5):
        if word[x] == solution[x]:
            letter_check.append("[O]")
        elif word[x] in solution:
            letter_check.append("[X]")
        else:
            letter_check.append("[ ]")
    print(letter_check)

# Getting users guess and making sure it is in the word list
def users_guess():
    user_guess = ""
    usable_guess = False
    while usable_guess == False:
        print("Please guess a word:")
        user_guess = input().lower()
        if user_guess in word_list:
            usable_guess = True
        else:
            print("Word not in list")
    return user_guess


game_intro()
users_guess = users_guess()
check_letters(users_guess, todays_word)
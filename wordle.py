# wordle
# eric johnson
# feb 17, 2022

from viewcontrol import *

todays_word = "shake"
word_list = ["shape", "shake", "shale", "shame", "shave", "shade"]
guess_count = 0


# Getting users guess and making sure it is in the word list
def users_guess():
    guess_count += 1
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

game_session = ViewControl()
game_session.game_intro()
users_guess = users_guess()
game_session.check_letters(users_guess, todays_word)
game_session.display_boardstate()
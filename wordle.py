# wordle
# eric johnson
# feb 17, 2022

from viewcontrol import *

todays_word = "shake"
word_list = ["shape", "shake", "shale", "shame", "shave", "shade"]


# Getting users guess and making sure it is in the word list
def input_guess():
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

for guess_count in  range(0, 6, 1):
    users_guess = input_guess()
    game_session.check_letters(users_guess, todays_word, guess_count)
    game_session.display_boardstate()
    if game_session.victory:
        print("YOU WIN! Congrats!\n\n")
        break
if game_session.victory == False:
    print("Better Luck Next Time\n\n")
# wordle
# eric johnson

class ViewControl:
    def __init__(self):
        self.boardstate = []

    # Game into rows, breaks up terminal to make it more readable
    def game_intro(self):
        print("\n" * 10)
        print("#" * 50 + "\n" + "#" * 50)
        print("\nWelcome to my version of Wordle!")
        print("\nQuick Tip:")
        print("[O] = Correct letter in correct position")
        print("[X] = Letter is in word, but wrong position\n")
        print("#" * 50 + "\n" + "#" * 50)
        print("\n")

    # Checks users guess against the days solution, returns "map" of guesses
    def check_letters(self, word, solution, guess_num):
        letter_check = []
        for x in range(5):
            if word[x] == solution[x]:
                letter_check.append("[O]")
            elif word[x] in solution:
                letter_check.append("[X]")
            else:
                letter_check.append("[ ]")
        self.boardstate.append([letter_check , solution])
        return letter_check

    def display_boardstate(self):
        print("\n")
        for x in range(0, 1, 1):
            print(str(self.boardstate[x][0]) + " -> " + str(self.boardstate[x][1]))
        print("\n")
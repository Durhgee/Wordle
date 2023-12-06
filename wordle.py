import random

def wordle():
    print("\nWelcome to 6-letter Wordle!\n"
          "You are allowed 6 guesses of 6-letter words.\n"
          "\033[31m" + "Red" + "\x1b[0m", "letters are correct letters, but in the wrong spot.", "\033[35m" + "Purple" + "\x1b[0m", "letters are correct letters in the correct spot. Gray letters are incorrect letters.\n"
          "Let the guessing commence!\n")

    letters = [ #creates a 2d list, where the first index choice is the letter, while the second index choice is the first, second, third, or fourth line of the ascii letter
        ["    db    ",
         "   dPYb   ",
         "  dPwwYb  ",
         " dP    Yb "], #a

        ["  888b.   ",
         "  8wwwP   ",
         "  8   b   ",
         "  888P'   "], #b

        ["  .d88b   ", "  8P      ", "  8b      ", "  `Y88P   "], #c
        ["  888b.   ", "  8   8   ", "  8   8   ", "  888P'   "], #d
        ["   8888   ", "   8www   ", "   8      ", "   8888   "], #e
        ["   8888   ", "   8www   ", "   8      ", "   8      "], #f
        ["  .d88b   ", "  8P www  ", "  8b  d8  ", "  `Y88P'  "], #g
        ["  8   8   ", "  8www8   ", "  8   8   ", "  8   8   "], #h
        ["   888    ", "    8     ", "    8     ", "   888    "], #i
        ["   8888   ", "     8    ", "  w  8    ", "  `Yw     "], #j
        ["  8  dP   ", "  8wdP    ", "  88Yb    ", "  8  Yb   "], #k
        ["   8      ", "   8      ", "   8      ", "   8888   "], #l
        [" 8b   d8  ", " 8YbmdP8  ", " 8  '  8  ", " 8     8  "], #m
        ["  8b  8   ", "  8Ybm8   ", "  8  '8   ", "  8   8   "], #n
        ["  .d88b.  ", "  8P  Y8  ", "  8P  Y8  ", "  `Y88P'  "], #o
        ["  888b.   ", "  8  .8   ", "  8wwP'   ", "  8       "], #p
        ["  .d88b.  ", "  8P  Y8  ", "  8b wd8  ", "  `Y88Pw  "], #q
        ["  888b.   ", "  8  .8   ", "  8wwK'   ", "  8  Yb   "], #r
        ["  .d88b.  ", "  YPwww.  ", "      d8  ", "  `Y88P'  "], #s
        ["  88888   ", "    8     ", "    8     ", "    8     "], #t
        ["  8    8  ", "  8    8  ", "  8b..d8  ", "  `Y88P'  "], #u
        [" Yb    dP ", "  Yb  dP  ", "   YbdP   ", "    YP    "], #v
        ["Yb      dP", " Yb db dP ", " YbdPYbdP ", "  YP  YP  "], #w
        ["  Yb  dP  ", "   YbdP   ", "   dPYb   ", "  dP  Yb  "], #x
        ["  Yb  dP  ", "   YbdP   ", "    YP    ", "    88    "], #y
        ["  8888P   ", "    dP    ", "   dP     ", "  d8888   "]] #z

    thisdict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
                "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    line_divider = "+----------+----------+----------+----------+----------+----------+"
    char_divider = "|          |          |          |          |          |          |"

    replay = True
    while replay == True:
        char_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        i = random.randint(0, 1002)
        with open("word_list.txt") as word_list:
            selected_word = word_list.readlines()
            selected_word = selected_word[i].strip()
        print(list(selected_word))

        attempts = 0
        guess_num = ["a"] * 6
        while attempts in range(6):
            guess = input("Guess: ")
            while len(guess) != 6 or not guess.isalpha():
                print("Please input a 6-letter word.")
                guess = input("Guess: ")

            with open("word_list.txt") as word_list:
                temp = word_list.readlines() #creates a list that contains all possible words from the word list
                for w in range(len(temp)):
                    temp[w] = temp[w].strip() # creates a list that contains all possible words, but without the \n
                while guess not in temp:
                    print("Please input a valid word.")
                    guess = input("Guess: ")

            guess_num[attempts] = guess #assigns an index in the list guess_num to the guessed word, so that past words can be printed before the guessed word
            list(guess) #creates a list of the letters in the guessed word

            for j in range(attempts + 1):
                print(line_divider)
                guess = guess_num[j]

                for n in range(4): #makes spot height 4 lines tall
                    for h in range(6): #creates 6 spots per row

                        print("|", end="") #prints the | before each letter

                        if guess[h].lower() == selected_word[h].lower(): #if the letter is correct and in the correct spot, print purple
                            print("\033[32m" + letters[thisdict[guess[h].lower()]][n] + "\x1b[0m", end="")
                            #guess[h] "returns" a letter in the guessed word
                            #thisdict[] "returns" a number to that letter
                            #letters[][n] "returns" the first, second, third, or fourth line of the ascii form of the letter

                        elif (guess[h].lower() == selected_word[0].lower() or
                              guess[h].lower() == selected_word[1].lower() or
                              guess[h].lower() == selected_word[2].lower() or
                              guess[h].lower() == selected_word[3].lower() or
                              guess[h].lower() == selected_word[4].lower() or
                              guess[h].lower() == selected_word[5].lower()): #if the letter is correct and in the incorrect spot, print red
                            print("\033[33m" + letters[thisdict[guess[h].lower()]][n] + "\x1b[0m", end="")

                        else: #print the letter in standard gray
                            print("" + letters[thisdict[guess[h].lower()]][n] + "", end="")

                        if guess[h] in char_bank:
                            char_bank.remove(guess[h])

                    print(end="|\n") #prints the | at the end of every line

            attempts += 1

            for i in range(attempts, 6): #prints blank spots
                print(line_divider)
                for e in range(4):
                    print(char_divider)
            print(line_divider)

            print("Unused letters: ", end="")
            for q in range(len(char_bank)):
                print(char_bank[q].upper(), end=" ")
            print()

            if attempts == 1 and guess.lower() == selected_word.lower():
                print("\nYou won in", attempts, "guess!")
                break
            elif guess.lower() == selected_word.lower():
                print("\nYou won in", attempts, "guesses!")
                break
            if attempts == 6:
                print("\nYou lost.")

        replay_response = input("\nPlay again? ")
        if replay_response.lower() == "yes" or replay_response.lower() == "y":
            replay = True
        else:
            replay = False

wordle()
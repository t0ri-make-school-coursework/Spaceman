import sys
import random

# Initiating function, welcomes player calls spaceman_start_ready().
def spaceman_start():
    print(chr(27) + "[2J")
    print("Welcome to Spaceman!")
    spaceman_start_ready()

# Checks if player is ready.
# If player is ready, select_category().
def spaceman_start_ready():
    ready = input("Are you ready to play? y/n: ").lower()
    if ready == "y":
        select_category()
    elif ready == "n":
        spaceman_start_player_not_ready()
    elif ready in ("quit","exit"):
        exit_game()
    else:
        invalid()

# Asks if player knows how to play.
# If player knows how to play, spaceman_start_ready()
def spaceman_start_player_not_ready():
    response = input("Do you know how to play? y/n: ").lower()
    if response == "y":
        exit_game()
    elif response == "n":
        rules()
        spaceman_start_ready()
    elif response in ("quit","exit"):
        exit_game()
    else:
        invalid()
        spaceman_start_ready()


# Prints the rules of Spaceman.
def rules():
    print("Spaceman is a guessing game! I will think of a word and you will try to guess"\
          "it by suggesting letters. You can only guess incorrectly seven times before you lose and the game ends!")

# Asks if the player wants to quit.
# If player wants to quit, game exits.
def exit_game():
    response = input("Do want to quit? y/n: ")
    if response in ("y", "exit", "quit"):
        print("Thanks for playing!")
        sys.exit()
    elif response == "n":
        spaceman_start_ready()
    else:
        invalid()
        spaceman_start_ready()

# If input is invalid, print "Invalid input!"
def invalid():
    print("Invalid input!")

# Categories Nested List, categories[num][0] is name of list, categories[num][1-num] is words in each category
categories = [["Tori's Favorite Colors", "marsala", "lilac"],
              ["Tori's Pets' Names", "charlotte", "elizabeth", "theodore", "maxwell", "callie"],
              ["Places Tori Has Been", "", ""]]

def select_category():
    print("Here are the categories:")
    i = 0

    for category in categories:
        print("Type \'{}\' to select {}".format(i, categories[i][0]))
        i += 1

    selection = int(input("Choose your category: "))
    print("You have selected the category {}!".format(categories[selection][0]))

    ready = input("Would you like to select a different category? y/n: ").lower()

    if ready == "n":
        random_word(selection)
    elif ready == "y":
        select_category()
    else:
        print("Invalid index!")
        select_category()

def random_word(category_index):
    word_index = random.randint(1,len(categories[category_index]) - 1)
    word = categories[category_index][word_index]

    get_letters(word)

letters = [[],[]]
guess_amount = 7
guesses = []
correctguesses = 0
complete = False


def get_letters(word):
    letters[0] = list(word)

    for i in letters[0]:
        letters[1].append("_")

    print_current_state(letters[1])

def print_current_state(the_letters):
    print(chr(27) + "[2J")
    print("Here's your word:")
    print(' '.join(the_letters))
    print("\n")

    take_guess()

def take_guess():
    guess = input("Type a letter to guess: ").lower()
    check_guess_type(guess)

def wrong_guess(guess):
    guesses.append("X")
    if len(guesses) >= guess_amount:
        end_game_lose()
    else:
        print(' '.join(guesses))
        print("No {}s here! Incorrect guesses: {} of {}".format(guess.upper(), len(guesses), guess_amount))
        print("\n")
        take_guess()


# Checks if input (w) is an int.
def is_int(l):
    try:
        int(l)
        return True
    except ValueError:
        return False

# Checks if input (w) is a float.
def is_float(l):
    try:
        float(l)
        return True
    except ValueError:
        return False

# Calls is_int() and is_float() to determine and reassign its type.
def check_guess_type(l):
    if "." not in l:
        if is_int(l):
            print("Int detected! Guess one letter.")
            take_guess()
    elif is_float(l):
        print("Float detected!  Guess one letter.")
        take_guess()

    if len(l) > 1:
        print("More than one letter detected!  Guess one letter.")
        take_guess()
    else:
        check_guess(l)

def letters_complete():
    if "_" not in letters[1]:
        return True
    else:
        return False

def check_guess(guess):
    global complete
    i = 0

    is_found = False

    for group in letters:
        for letter in group:
            if guess == letters[0][i]:
                letters[1][i] = guess
                print("Good guess! Adding a {} to the word!".format(guess.upper()))

                is_found = True

                print(letters_complete())
                if letters_complete():
                    end_game_win()

            i += 1

        if not is_found:
            wrong_guess(guess)

        print_current_state(letters[1])

    take_guess()

def end_game_win():
    print("Congratulations! You win Spaceman!")
    sys.exit()

def end_game_lose():
    print("You lose :(")
    sys.exit()

spaceman_start()

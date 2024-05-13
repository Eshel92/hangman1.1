HANGMAN_ASCII_ART = ("""welcome to  the game hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ 

                     """)
num_of_tries = 0
MAX_TRIES = 6
print(HANGMAN_ASCII_ART, MAX_TRIES)
HANGMAN_PHOTOS = {
    0: (r"""
    x-------x """),
    1: (r"""
    x-------x
    |
    |
    |
    |
    |

"""),
    2: (r"""
    x-------x
    |       |
    |       0
    |
    |
    |
"""),
    3: (r"""
    x-------x
    |       |
    |       0
    |       |
    |
    |
"""),
    4: (r"""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
"""),
    5: r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
""",
    6: r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
""",
}


def check_valid_input(letter_guessed, old_letters_guessed):
    """this function gets the input and the list of the letters guessed and check if the input is valid"""
    if letter_guessed in old_letters_guessed:  # checking if it was already guessed
        return False
    elif len(letter_guessed) > 1:  # checking if It's nothing
        return False
    elif len(letter_guessed) == 1 and (letter_guessed < 'A' or letter_guessed > 'z'):  # checking if it's a letter
        return False
    else:
        print(letter_guessed.lower())
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    """this function tries to update the list of the letters guessed"""
    global num_of_tries
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())  # appends the guess to the letters guessed
        if letter_guessed.lower() not in secret_word:  # in case the letter is wrong
            num_of_tries += 1  # updates the num of tries
            print(':(')
            print("num of tries =", num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))

    else:  # if input is not valid print X and a sorted list of the letters that were guessed
        print("X")
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """this function shows the hidden word with the letters the player guessed"""
    st = ""
    for guess in secret_word:
        if guess in old_letters_guessed:
            st += guess + " "
        else:
            st += "_ "
    return st


def check_win(secret_word, old_letters_guessed):
    """this function gets the secret word, and the list of the letters guessed and checks for win"""
    for guess in secret_word:
        if guess not in old_letters_guessed:
            return False
    print("you won!!!!!!!!")
    return True


def print_hangman(number_of_tries):
    """this function gets the number of tries and prints the drawing of the hangman"""
    print(HANGMAN_PHOTOS[number_of_tries])


def choose_word(file_path, index):
    """this function gets the file path and index and chooses the word from the file for the game"""
    file1 = open(file_path, 'r')
    file_read = file1.read()
    list1 = list(file_read.split("\n"))  # splitting by \n,the file is a list of words one on top of each other
    file1.close()
    return list1[index]


def word_len(secret_word):
    return '_ ' * len(secret_word)


def main():
    try:
        global num_of_tries  # get the num of tries
        try:
            secret_word = choose_word(input(r"Please enter file path: ").lower(), int(input(r"Please enter index: ")))
        except FileNotFoundError:  # check for file not found
            print("file not found")
            exit(1)
        except ValueError as e:  # check for value errors
            print(f"value error: {e}")
            exit(1)
        except IndexError:  # check for index out of range
            print("index out of range:")
            exit(1)
        old_letters_guessed = []
        print('Lets start!')
        print(word_len(secret_word))
        while num_of_tries < MAX_TRIES:  # the loop that manages the game
            print_hangman(num_of_tries)
            try_update_letter_guessed(input('Enter a letter: '), old_letters_guessed, secret_word)
            show_hidden_word(secret_word, old_letters_guessed)  # shows the updated line of the word with the letters
            game_status = check_win(secret_word, old_letters_guessed)  # checks for win
            if game_status:
                break
        if not game_status:
            print('lose!')
            print("secret word is", secret_word)
    except KeyboardInterrupt:
        print("\ngame stopped by user")
    except Exception as e:
        print(f"there was an error {e}")


if __name__ == "__main__":
    main()

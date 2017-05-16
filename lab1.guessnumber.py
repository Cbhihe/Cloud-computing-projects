""" Lab1.guessnumber.py based on Python v2.7  """

import random

# State constants
ABORTED = 0
GUESSED_RIGHT = 1
GUESSED_WRONG = 2

# Guess boundaries
MIN_GUESS = 1
MAX_GUESS = 20

# Format the question text
QUESTION = "Guess a number between {} and {}: ".format(MIN_GUESS, MAX_GUESS)

# init the random number
# Outside a block or a definition the variable name should be capitalized.
GUESS_NUM = random.randint(MIN_GUESS, MAX_GUESS)

# Starts the game
# Returns True if guessed correctly else false
def game_round():
    """ --- """
    try:
        inputstring = raw_input(QUESTION)

        # Abort
        if inputstring == "exit":
            return ABORTED

	# parse guess
        guess = int(inputstring)

	# Guess out of boundaries
        if guess < MIN_GUESS or guess > MAX_GUESS:
            return GUESSED_WRONG

	# Guess too high
        if guess > GUESS_NUM:
            print "Your guessed number is too high."
            return GUESSED_WRONG

	# Guess too low
        if guess < GUESS_NUM:
            print "Your guessed number is too low."
            return GUESSED_WRONG

    except ValueError:
        # Handle any ValueError exception
        print "Write a valid integer."
        return GUESSED_WRONG

    return GUESSED_RIGHT

# The game function
def game():
    """ --- """
    state = GUESSED_WRONG
    while state == GUESSED_WRONG:
        state = game_round()

        if state == ABORTED:
            print "Thanks for playing! Good luck next time!"
        elif state == GUESSED_RIGHT:
            print "You guessed {} well!".format(GUESS_NUM)

# Only runs game() if script is executed directly by passing it
#   as cmd to python interpreter
# Only if file is executed directly, is __name__ set to __main__
if __name__ == "__main__":
    print "Welcome to \"Guess the number!\"\nTo abort the game write \"exit\"."
    game()

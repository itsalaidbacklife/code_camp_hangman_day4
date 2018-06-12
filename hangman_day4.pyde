from HangmanFile import Hangman

hangman = Hangman('secret')

def setup():
    size(1000, 1000)
    global show_guy, correct_guesses, incorrect_guesses, word
    show_guy = False
    correct_guesses = []
    incorrect_guesses = []
    word = "secret" #The secret word
    
    #set up correct guesses to have blank spaces for each missing letter
    for x in range(len(word)):
        correct_guesses.append("--")
    
def draw():
    hangman.display()
def keyPressed():
    global hangman
    if not hangman.gameOver:
        hangman.guess(key)
    else:
        hangman = Hangman('wittershins')
    
def guess(letter):
    global correct_guesses, incorrect_guesses, word
    in_word = False
    for index, x in enumerate(word):
        if letter == x:
            correct_guesses[index] = letter
            in_word = True
    if not in_word:
        incorrect_guesses.append(letter)
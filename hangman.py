# Hangman game
# This program was created as a part of the MITx 6001 course

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = list()
    for letter in secretWord:
        if letter in lettersGuessed:
            x.append(True)
        else:
            x.append(False)
    if False in x:
        return False
    else:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    y = str()
    for letter in secretWord:
        if letter in lettersGuessed:
            y = y + letter
        else:
            y = y + '_ '
    return y

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lettersLeft = string.ascii_lowercase

    for letter in lettersGuessed:
        if letter in lettersLeft:
            lettersLeft = lettersLeft.replace(letter, '')
    return lettersLeft


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = list()
    numGuesses = 8
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')

    for i in range(numGuesses):
        print('You have',numGuesses,'guesses left.')
        print('Available letters: ', getAvailableLetters(lettersGuessed))
        inp = input('Please guess a letter: ').lower()
        if inp in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        else:
            lettersGuessed.append(inp)
            if inp in secretWord:
                print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                if isWordGuessed(secretWord, lettersGuessed):
                    print('Congratulations, you won!')
                    return
            else:
                numGuesses -= 1
                print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
    print('Sorry, you ran out of guesses. The word was', secretWord)
    return

secretWord = 'python'
#secretWord = chooseWord(wordlist).lower()
print(hangman(secretWord))

# Hangman game
#

# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    l=list(secretWord)
    a=0
    for w in l:
        if w in lettersGuessed:
            a+=1
    if a==len(l):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
   
    l=list(secretWord)
    a=0
    for w in l:
        if w not in lettersGuessed:
            b=l.index(w)
            l[b]=" _ "
    return "".join(l)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    s=string.ascii_lowercase
    l=list(s)
    l2=l[:]
    for e in l2:
        if e in lettersGuessed:
            l.remove(e)
    return "".join(l)
    





def wordcheck(secretWord, lettersGuessed):
    l=list(secretWord)
    for c in lettersGuessed:
        if c in l:
            return True
        else:
            return False



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
    
   
    print("Welcome to the game Hangman!")
    word=secretWord
    print("I am thinking of a word that is "+str(len(word))+" letters long.")
    guesses=8
    guesslist1=[]
    guesslist2=[]
    totalLetters=string.ascii_lowercase
    hope=1
    while hope==1:
        print("-------------")
        print("You have "+str(guesses)+" guesses left.")
        print("Available letters: "+getAvailableLetters(guesslist1))
       
        guess=input("Please guess a letter: ")
        
        
        guess=guess.lower()
        if guess in guesslist1:
            print("Oops! You've already guessed that letter: "+getGuessedWord(word, guesslist2))
        else:
            guesslist1.append(guess)
            check=wordcheck(word, guess)
            if check==True:
                guesslist2.append(guess)
            
            
            
                print("Good guess: "+getGuessedWord(word, guesslist2))
                if getGuessedWord(word, guesslist2)==word:
                    print("------------")
                    print("Congratulations, you won!")
                    hope=0
            else:
            
            
                guesses-=1
                print("Oops! That letter is not in my word: "+getGuessedWord(word, guesslist2))
            if guesses==0:
                print("-----------")
                print("Sorry, you ran out of guesses. The word was "+word+".")
                hope=0
    








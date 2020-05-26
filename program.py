import time
from random_words import RandomWords
#RandomWords is a useful package for generate random words, nicks, e-mails and lorem ipsum.

name = raw_input('What is your name?')
print "Hello " + name + " Let's play the hangman game !"
time.sleep(0.5)
print""
rw = RandomWords()
secret_word = rw.random_word()
chances = len(secret_word)
print "You have", +chances, "chances to guess the word right!"
time.sleep(0.5)

guesses = ""

while chances > 0:
    wrong = 0
    for letter in secret_word:
        if letter in guesses:
            print letter,
        else:
            print "_",
            wrong += 1

    print ""
    if wrong == 0:
        print "YOU WON !"

        #exit the script
        break

    print ""

    guess = raw_input("Guess a character : ")

    if guess in guesses:
        print "This letter is already printed, please guess another letter"
        print ""

    guesses += guess

    if guess not in secret_word:
        chances -= 1
        print "Oops ! wrong guess"

        if chances == 0:
            print "You lost !",
            print "it was: " + secret_word
        else:
            print "You've got", +chances, "chances left"

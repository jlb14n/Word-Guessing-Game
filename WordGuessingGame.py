#Initialization
word="word"
letter=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
guess_let=set()
guess_num=7
win=False
print("Welcome to the Word Guessing Game!")

#The game itself:
while guess_num>0:
    #Print word
    temp_print=""
    for i in range(0, len(word)):
        if word[i] in guess_let:
            temp_print+=word[i] + " "
        else:
            temp_print+="_ "
    print(temp_print)

    #User input
    print("You have {0} guesses remaining!".format(guess_num))
    invalid=True
    while invalid: #Checking correct type of entry
        guess=input("Input your guess (a letter or word): ")
        if len(guess)==len(word):
            invalid=False
            if guess==word:
                win=True
                break
        if len(guess)==1 and guess in letter:
            if guess in guess_let:
                print("You've guessed that before!")
            else:
                invalid=False
                guess_let.add(guess)
            if set(word).issubset(guess_let):
                win=True
                break
        else:
            print("Invalid entry")
    guess_num-=1
    if win:
        break
else:
    print("You lose :(")
    print("The word was '{0}'".format(word))
if win:
    print("You won with {0} guesses remaining!".format(guess_num))
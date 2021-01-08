import random
import wordfile 

def hungman(wrong_guess):
    if wrong_guess == 0:
        print("_________\n|")
    if wrong_guess == 1:
        print("_________\n|\no")
    if wrong_guess == 2:
        print("_________\n|\no\n|\n|")
    if wrong_guess == 3:
        print("_________\n |\n o\n\|\n |")
    if wrong_guess == 4:
        print("_________\n |\n o\n\|\n |")
    if wrong_guess == 5:
        print("_________\n |\n o\n\|/\n |\n/")
    if wrong_guess == 6:
        print("_________\n |\n o\n\|/\n |\n/|\\")
        print("YOU LOST!")
        print("THE WORD WAS", selected_word[0])
        play_again = input("if you want to play again please enter yes or no: ")


play_again = "yes"

while play_again == "yes":
    def getword():
        words = ["lion","cow","monkey","buffalow","zebra","crocodile","giraffe","elephant","bull","peacock","kingfisher"]

        word = random.choices(words)
        return word


    selected_word = getword()

    print("COME ON GUESS", "\nHINT:an animal")

    print("_  " * len(selected_word[0]))

    answer = "_" * len(selected_word[0])
    answer = list(answer)

    wrong_guess = 0
    j = 0
    while True:
        if wrong_guess > 6:
            break
        if ("").join(answer) == selected_word[0]:
            print("YOU ARE INSANE... YOU WIN")
            print("The word is ", ("").join(answer).upper())
            play_again = input("come lets play again enter yes or i know you are a busy... person enter no: ")
            if play_again == "yes":
                selected_word = getword()
            break

        guess = input("Enter your guess ")
        if guess in selected_word[0]:
            for i in range(len(selected_word[0])):
                if selected_word[0][i] == guess:
                    answer[i] = guess
            print("Your guess is correct")
            print(answer)
        else:
            print("your guess is wrong")
            hungman(wrong_guess)
            wrong_guess += 1

import random
def welcome():
    print("WELCOME TO THE NUMBER GUESS GAME")

number_to_guess = random.randint(1, 10)

welcome()
def fun1():
    count_number_of_tries = 1
    guess = int(input("plesase guess a number between 1 and 10: "))
    while number_to_guess != guess:
        print("sorry wrong number")
        if count_number_of_tries == 4:
                break
        elif guess < number_to_guess:
            print("your guess was lower than the number")
        else:
            print("your guess was higher than the number")
        guess = int(input("please guess again: "))
        count_number_of_tries += 1


    if number_to_guess == guess:
        print("well done you won!")
        print("you took ", count_number_of_tries," goes to complete the game")
    else:
        print("sorry - you loose")
        print("the number you needed to guess was ", number_to_guess)
    print("game over")

fun1()
from random import randint


#Game setup

print("Welcome to the Guessing Game")
guesses = 3
user_won = False

#Computer gets a random number between 1 and 10
random_integer = randint(1,10)

#User guesses the number

while guesses > 0:
    user_guess = int(input("Guess my number: (guesses remaining " + str(guesses) + ") "))
    print(user_guess)
    if user_guess == random_integer:
        print("That is correct!")
        user_won = True
        break
    elif user_guess < random_integer:
        guesses -= 1
        if guesses > 0:
            print("Too low. Try again.")
    else:
        guesses -= 1
        if guesses > 0:
            print("Too high. Try again.")

#Win or lose statement to the user
if user_won == True:
    print("You Won!")
else:
    print("Sorry you dont have anymore guesses. You lose.")

#Computer tells the user whether guess was too high or too low
#User has 3 guesses

def guess_me(): # defining a function called guess_me

    from random import randint #importing the randint function from the random module to generate a random number

    secret_number = randint(1,10) #generating a random number between 1 and 10 and assigning it to the variable secret_number
    
    counter = 0 #defining a variable called counter and initializing it to 0 to keep track of the number of guesses

    while True:
        guess = input("I'm thinking of a number between 1 and 10. Can you guess it? ") #asking the user to input their guess and storing it in the variable guess
        counter += 1 #incrementing the counter variable by 1 each time the user makes a guess

        try: #running a try block to attempt to convert the user's guess to an integer
            guess = int(guess)
        except ValueError: #if the conversion fails, a ValueError will be raised, and we can catch it to handle the error gracefully
            print("Please enter a valid number between 1 and 10. Try again!")
            continue

        if not 1 <= guess <= 10: #checking if the user's guess is between 1 and 10. If it's not, we prompt them to enter a valid number
            print("Please enter a valid number between 1 and 10. Try again!") #if the user's guess is not between 1 and 10, we prompt them to enter a valid number
            continue
        

        match guess:
            case guess if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
            case guess if guess > secret_number:
                print("Too high! Give it another shot!")
            case _: # if otherwise, it means the guess is correct!
                print("Congratulations, you guessed it!")
                break
    print("You guessed {} times! ".format(counter)) #after the user guesses the correct number, we print out how many guesses it took them to get it right

    another_trial = input("\nPlay again? (yes/no)") # Promting the user to play again.
    if another_trial.lower() == "yes":
        guess_me()
    else:
        print("Thanks for playing! Goodbye! ") 

guess_me() #calling the funtion.
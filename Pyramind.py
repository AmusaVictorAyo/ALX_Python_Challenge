def printing_pyramid():

    # Checking for invalid input and correction!
    while True:

        print("\nWelcome! This program will create a pyramid of stars with the number of rows you enter.")
        rows = input("Enter a number from 1 to 10: ")

        try:
            rows =  int(rows)
        except ValueError:
            print("\nYou have entered an invalid value! Please try again. \n")
            continue
        
        if  not 1 <= rows <= 10:
            print("\nInput only between 1 and 10!\n")
            continue
        else:
            break

    print() # Printing new line
    current_row = 1

    while current_row <= rows:
        spaces = rows - current_row
        stars  = 2 * current_row -1

        # Printing Spaces
        space_counter = 0
        while space_counter < spaces:
            print(" ", end="")
            space_counter += 1
    
        # Printing stars
        star_counter = 0
        while star_counter < stars:
            print("*", end="")
            star_counter += 1

        print() #Printing new line

        current_row += 1
 
    while True:
        again = input("\nDo you want to try again? (y/n): ")
        if again.lower() == 'y':
            printing_pyramid()
        elif not again.lower() == 'n':
            print("Input only y/n! Please try again.")
            continue
            
        else:
            print("\nThanks for playing! Goodbye!")  
        break
printing_pyramid()
 


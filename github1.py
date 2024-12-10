import random  # Importing the random module for generating computer's moves

# Dictionary to store the symbols for computer and person
symbols = {'computer': 'X', 'person': 'O'}

# Taking input from the user to determine who will play first
player = input("Who will play first, computer or person: ")

# Initializing the tic tac toe board as a 3x3 matrix filled with `1`
a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

# Displaying the initial state of the tic tac toe board
print("Initial tic tac toe board:")
for i in a:
    print(i)

flag = 0  # To check if the game is won
renter = 1  # To check if the move is valid

# Proceed with the game only if the player's input matches the dictionary keys
if player in symbols.keys():
    while flag != 1:  # The game continues until someone wins or a tie is declared
        print(f"The player now playing is {player}")
        
        # If the current player is 'person', take input for row and column
        if player == 'person':
            row = int(input("Enter the row (0-2) in which you want to make a move: "))
            column = int(input("Enter the column (0-2) in which you want to make a move: "))
        else:
            # Computer generates a random move
            row = random.randint(0, 2)
            column = random.randint(0, 2)

        # Check if the chosen cell is empty
        if a[row][column] == 1:
            # Update the board with the player's symbol
            a[row][column] = symbols[player]
            renter = 1  # Valid move
        else:
            # Cell already occupied, prompt to re-enter
            print("Invalid move. Cell already occupied. Please re-enter.")
            renter = 0  # Invalid move
        
        # Check for win conditions for the computer ('X')
        if ((a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X') or
            (a[0][0] == 'X' and a[0][1] == 'X' and a[0][2] == 'X') or
            (a[0][2] == 'X' and a[1][1] == 'X' and a[2][0] == 'X') or
            (a[1][0] == 'X' and a[1][1] == 'X' and a[1][2] == 'X') or
            (a[2][0] == 'X' and a[2][1] == 'X' and a[2][2] == 'X') or
            (a[0][0] == 'X' and a[1][0] == 'X' and a[2][0] == 'X') or
            (a[0][1] == 'X' and a[1][1] == 'X' and a[2][1] == 'X') or
            (a[0][2] == 'X' and a[1][2] == 'X' and a[2][2] == 'X')):
            print("Hey! The computer won the game! Congratulations to AI!")
            exit(0)
        
        # Check for win conditions for the person ('O')
        elif ((a[0][0] == 'O' and a[1][1] == 'O' and a[2][2] == 'O') or
              (a[0][0] == 'O' and a[0][1] == 'O' and a[0][2] == 'O') or
              (a[0][2] == 'O' and a[1][1] == 'O' and a[2][0] == 'O') or
              (a[1][0] == 'O' and a[1][1] == 'O' and a[1][2] == 'O') or
              (a[2][0] == 'O' and a[2][1] == 'O' and a[2][2] == 'O') or
              (a[0][0] == 'O' and a[1][0] == 'O' and a[2][0] == 'O') or
              (a[0][1] == 'O' and a[1][1] == 'O' and a[2][1] == 'O') or
              (a[0][2] == 'O' and a[1][2] == 'O' and a[2][2] == 'O')):
            print("Congratulations! The person won against the computer!")
            exit(0)
        
        # Switch players if the move was valid
        if player == 'person' and renter == 1:
            player = 'computer'
        elif player == 'computer' and renter == 1:
            player = 'person'

        # Display the updated tic tac toe board
        print("The latest tic tac toe board is:")
        for i in a:
            print(i)

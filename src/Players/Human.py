from Move import Move
from Player import Player


class Human(Player):
    
    # Gets input from the user, asserts that it is valid, and return the Move object     
    def get_move(self, gamestate):
        move_found = False
        while not move_found:
            coords = input("Enter two coordinates <white> <black> (e.g., A1 A2): ").split()

            # Check if the user entered two coordinates
            if len(coords) != 2:
                print("You must enter exactly two coordinates.")
                continue

            # Check if the coordinates are 2 characters long
            if not (len(coords[0]) == 2 and len(coords[1]) == 2):
                print("Each coordinate should be 2 characters long.")
                continue

            col1, row1 = coords[0][0], coords[0][1]
            col2, row2 = coords[1][0], coords[1][1]

            # Check if the first character is a letter A-I and the second character is a digit 0-8
            if not (col1.isalpha() and col2.isalpha() and row1.isdigit() and row2.isdigit()):
                print("Coordinates should start with a letter (A-I) followed by a number (0-8).")
                continue
            
            # Convert to zero-indexed integers
            row1, col1, row2, col2 = int(row1), ord(col1) - ord('A'), int(row2), ord(col2) - ord('A')
            
            # Check if the coordinates are within the valid range
            if not all(0 <= n <= 8 for n in [row1, col1, row2, col2]):
                print(f"Coordinates ({row1}, {col1}) and ({row2}, {col2}) are out of the valid range.")
                continue
            
            # Check if coordinates are adjacent (horizontally or vertically)
            if not (row1 == row2 and abs(col1 - col2) == 1) and not (col1 == col2 and abs(row1 - row2) == 1):
                print(f"Coordinates ({row1}, {col1}) and ({row2}, {col2}) are not adjacent.")
                continue

            # Check occupation
            if gamestate.board[row1][col1] != 0 or gamestate.board[row2][col2] != 0:
                print("You cannot place a piece on an occupied square.")
                continue

            return Move(row1, col1, row2, col2)
        
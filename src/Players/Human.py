from Move import Move
from Player import Player


class Human(Player):
    def convert_input_to_coordinates(self, coords1, coords2):
        while True:
            user_input = input("Enter two coordinates (e.g., A1 A2): ")
            coord1, coord2 = user_input.split()

            if not (len(coord1) == 2 and len(coord2) == 2):
                print("Each coordinate should be 2 characters long.")
                continue

            col1, row1 = coord1[0], coord1[1]
            col2, row2 = coord2[0], coord2[1]

            # Check if the first character is a letter A-I and the second character is a digit 0-8
            if not (col1.isalpha() and col2.isalpha() and row1.isdigit() and row2.isdigit()):
                print("Coordinates should start with a letter (A-I) followed by a number (0-8).")
                continue

            col1, col2 = col1.upper(), col2.upper()

            if not ('A' <= col1 <= 'I' and 'A' <= col2 <= 'I' and '0' <= row1 <= '8' and '0' <= row2 <= '8'):
                print("Column must be between A-I and row must be between 0-8.")
                continue
            
            # Convert to zero-indexed integers
            row1, col1, row2, col2 = int(row1), ord(col1) - ord('A'), int(row2), ord(col2) - ord('A')
            return row1, col1, row2, col2
    
    def get_move(self, gamestate):

        move_found = False
        while not move_found:       
            row1, col1, row2, col2 = list(map(int, input().split()))
            
            # Check boundaries
            if row1 < 0 or row1 > 8:
                continue
            if row2 < 0 or row2 > 8:
                continue
            if col1 < 0 or col1 > 8:
                continue
            if col2 < 0 or col2 > 8:
                continue
            
            # Check adjacency
            if abs(row1 - row2) == 1 and abs(col1 - col2) != 0:
                continue
            if abs(row1 - row2) != 0 and abs(col1 - col2) == 1:
                continue
            
            # Check occupation
            if gamestate.board[row1][col1] != 0 or gamestate.board[row1][col1] != 0:
                continue


            return Move(row1, col1, row2, col2)
        
        
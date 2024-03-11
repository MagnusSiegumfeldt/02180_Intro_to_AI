class Move:
    def __init__(self, row1, col1, row2, col2):
        # coordinate 1 is white, 2 is black
        self.row1 = row1
        self.col1 = col1
        self.row2 = row2
        self.col2 = col2

    def __str__(self):
        # Convert column numbers to letters
        col1_letter = chr(self.col1 + ord("A"))
        col2_letter = chr(self.col2 + ord("A"))

        # Create string representation
        coord1 = f"{col1_letter}{self.row1}"
        coord2 = f"{col2_letter}{self.row2}"
        return f"({coord1} to {coord2})"

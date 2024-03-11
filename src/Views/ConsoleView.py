from View import View


class ConsoleView(View):
    def __init__(self):
        self.int_to_char = {0: "-", 1: "■", 2: "□"}
        pass

    def show(self, game):
        col_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        row_labels = [str(i) for i in range(9)]

        # Print column headers
        print("  " + " ".join(col_labels))

        # Print rows with their labels
        for label, row in zip(row_labels, game.board):
            print(f"{label} " + " ".join(self.int_to_char[cell] for cell in row))
    
    def update(self, gamestate):
        pass

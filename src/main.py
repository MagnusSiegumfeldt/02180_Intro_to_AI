import sys

from Views.GuiView import GuiView
from Views.ConsoleView import ConsoleView
from Runner import run_game


def main():
    if len(sys.argv) != 5:
        print(
            "Usage: python main.py <player1> <player2> <player1_depth> <player2_depth>"
        )
        print(
            "MinimaxArea: 0\nMinimaxAlphaBeta: 1\nMiniMaxAlphaBetaHashing: 2\nMiniMaxAlphaBetaHashingAdvanced: 3"
        )
        return

    p1 = sys.argv[1]
    p2 = sys.argv[2]
    p1d = sys.argv[3]
    p2d = sys.argv[4]

    run_game(int(p1), int(p2), int(p1d), int(p2d), None, True)
    return


if __name__ == "__main__":
    main()

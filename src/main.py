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


def print_turn_record(turn_stats):
    print("Turn number:", turn_stats[0])
    print("Time taken:", turn_stats[1])
    print("Nodes visited:", turn_stats[2])
    print("Player color: ", turn_stats[3])
    print(f"Score: {turn_stats[4]} => {sum(turn_stats[4][0]) - sum(turn_stats[4][1])}")
    print("\n")


if __name__ == "__main__":
    main()

import time as t
import sys

from GameState import GameState
from Players.ConsolePlayer import ConsolePlayer
from Players.GuiPlayer import GuiPlayer
from Players.MinimaxArea import MinimaxArea
from Players.MinimaxAlphaBeta import MinimaxAlphaBeta
from Players.MiniMaxAlphaBetaHashing import MiniMaxAlphaBetaHashing
from Players.MinimaxAlphaBetaHashingAdvanced import MiniMaxAlphaBetaHashingAdvanced
from Views.GuiView import GuiView
from Views.ConsoleView import ConsoleView
from Runner import run_game

def main():
    if len(sys.argv) != 5:
        print("Usage: python main.py <player1> <player2> <player1_depth> <player2_depth>")
        print("player1 and player2 are integers from 0 to 3")
        print("player1_depth and player2_depth are integers")
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

import time as t

from GameState import GameState
from Players.ConsolePlayer import ConsolePlayer
from Players.GuiPlayer import GuiPlayer
from Players.MinimaxArea import MinimaxArea
from Players.MinimaxAlphaBeta import MinimaxAlphaBeta
from Views.GuiView import GuiView
from Views.ConsoleView import ConsoleView


def main():
    view = GuiView()
    player1 = MinimaxAlphaBeta(color=1, depth=2)
    player2 = MinimaxAlphaBeta(color=2, depth=2)
    game = GameState(player1, player2)
    current_player = player1

    # List of tuples (turn_number, move_time, number_of_nodes_visited, player_turn, score)
    game_records = []

    while not game.finished():
        start = t.perf_counter()
        view.show(game)
        move = current_player.get_move(game)
        try:
            game.make_move(move)
            view.update(move)   
        except:
            print("Invalid move", move)
            return
        
        turn_record = (len(game_records) + 1, t.perf_counter() - start, current_player.nodes_visited, current_player.color, game.score())
        print_turn_record(turn_record)
        game_records.append(turn_record)

        current_player = player1 if current_player == player2 else player2

    view.show(game)
    print("Game over")
    print("Final score:", game.score())

def print_turn_record(turn_stats):
    print("Turn number:", turn_stats[0])
    print("Time taken:", turn_stats[1])
    print("Nodes visited:", turn_stats[2])
    print("Player color: ", turn_stats[3])
    print(f"Score: {turn_stats[4]} => {sum(turn_stats[4][0]) - sum(turn_stats[4][1])}")
    print("\n")


if __name__ == "__main__":
    main()

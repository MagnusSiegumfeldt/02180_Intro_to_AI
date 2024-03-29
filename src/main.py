from Players.MinimaxArea import MinimaxArea
from Players.MinimaxAlphaBeta import MinimaxAlphaBeta
from Players.MiniMaxAlphaBetaHashing import MiniMaxAlphaBetaHashing
from Players.MinimaxAlphaBetaHashingAdvanced import MiniMaxAlphaBetaHashingAdvanced
from Players.GuiPlayer import GuiPlayer
from Views.GuiView import GuiView
from Views.ConsoleView import ConsoleView
from GameState import GameState

import cProfile

def main():
    view = GuiView()

    player1 = GuiPlayer(view)
    player2= MiniMaxAlphaBetaHashingAdvanced(color=2, depth=2)
    game = GameState(player1, player2)

    current_player = player1

    while not game.finished():
        view.show(game)
        with cProfile.Profile() as pr:
            
            move = current_player.get_move(game)
            try:
                game.make_move(move)
                view.update(move)
            except:
                print("Invalid move", move)
                return
            
            score = game.score()
            #print(f"Player 1:\t{score[0][0]} + {score[0][1]} = {score[0][0] + score[0][1]}")
            #print(f"Player 2:\t{score[1][0]} + {score[1][1]} = {score[1][0] + score[1][1]}")
            current_player = player1 if current_player == player2 else player2
        pr.print_stats()
    view.show(game)
    print("Game over")


if __name__ == "__main__":
    main()

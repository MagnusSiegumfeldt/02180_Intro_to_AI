from GameState import GameState
from Players.Human import Human
from Players.GuiPlayer import GuiPlayer
from Players.MinimaxArea import MinimaxArea
from Players.MinimaxAlphaBeta import MinimaxAlphaBeta
from Views.GuiView import GuiView
from Views.ConsoleView import ConsoleView


def main():
    view = GuiView()
    player1 = GuiPlayer(view)
    player2 = MinimaxAlphaBeta(color=2, depth=2)
    game = GameState(player1, player2)

    current_player = player1
    while not game.finished():
        view.show(game)
        move = current_player.get_move(game)
        try:
            game.make_move(move)
            view.update(move)
        except:
            print("Invalid move", move)
            return
        score = game.score()
        print(f"Player 1:{score[0][0]} + {score[0][1]} = {score[0][0] + score[0][1]}")
        print(f"Player 2:{score[1][0]} + {score[1][1]} = {score[1][0] + score[1][1]}")
        current_player = player1 if current_player == player2 else player2
    view.show(game)
    print("Game over")


if __name__ == "__main__":
    main()

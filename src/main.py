from GameState import GameState
from Players.Human import Human
from Players.GuiPlayer import GuiPlayer
from Players.MinimaxArea import MinimaxArea
from Views.GuiView import GuiView




def main():
    view = GuiView()
    player1 = GuiPlayer(view)
    player2 = MinimaxArea(color=2, depth=2)
    game = GameState(player1, player2)

    current_player = player1
    while not game.finished():
        view.show(game) 
        
        # Get move from current players
        move = current_player.get_move(game)
        print("got move", move)
        
        # Implement move
        try:
            game.make_move(move)
            view.update(move.col1,move.row1,move.col2,move.row2)

        except:
            print("Invalid move", move)
            return 
        # Swap who's turn it is
        current_player = player1 if current_player == player2 else player2
    view.show(game)
    print("Game over")

if __name__ == "__main__":
    main()





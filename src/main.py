from GameState import GameState

from Players.Human import Human
from Views.ConsoleView import ConsoleView





def main():
    player1 = Human()
    player2 = Human()
    view = ConsoleView()
    game = GameState(player1, player2)

    current_player = player1
    while not game.finished():
        view.show(game)
        
        # Get move from current players
        move = current_player.get_move(game)
        print("got move", move)
        # Implement move
        game.make_move(move)

        # Swap who's turn it is
        current_player = player1 if current_player == player2 else player2



if __name__ == "__main__":
    main()




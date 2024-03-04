from GameState import GameState
from Players.Human import Human
from Players.TheDrunkenFool import TheDrunkenFool
from Views.ConsoleView import ConsoleView


def main():
    player1 = TheDrunkenFool()
    player2 = TheDrunkenFool()
    view = ConsoleView()
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
        except:
            print("Invalid move", move)
            continue
        # Swap who's turn it is
        current_player = player1 if current_player == player2 else player2
    view.show(game)
    print("Game over")

if __name__ == "__main__":
    main()

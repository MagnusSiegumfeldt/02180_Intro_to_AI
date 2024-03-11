# Runner.py
import time as t
from Players.MinimaxArea import MinimaxArea
from Players.MinimaxAlphaBeta import MinimaxAlphaBeta
from Players.MiniMaxAlphaBetaHashing import MiniMaxAlphaBetaHashing
from Players.MinimaxAlphaBetaHashingAdvanced import MiniMaxAlphaBetaHashingAdvanced
from GameState import GameState

player_map = {
  0: MinimaxArea,
  1: MinimaxAlphaBeta,
  2: MiniMaxAlphaBetaHashing,
  3: MiniMaxAlphaBetaHashingAdvanced
}

def run_game(p1, p2, p1d=2, p2d=2, view=None, verbose=True):

  player1 = player_map[p1](color=1, depth=p1d)
  player2 = player_map[p2](color=2, depth=p2d)
  game = GameState(player1, player2)

  current_player = player1
  game_records = []

  if verbose:
     print_start_of_game(game)
     
  while not game.finished():
      start = t.perf_counter()
      move = current_player.get_move(game)
      try:
          game.make_move(move)
      except:
          print("Invalid move", move)
          return

      if view:
        view.show(game)
        view.update(move)   

      turn_record = (len(game_records) + 1, t.perf_counter() - start, current_player.nodes_visited, current_player.color, game.score())
      if verbose:
        print_turn_record(turn_record)
      game_records.append(turn_record)

      current_player = player1 if current_player == player2 else player2

  view.show(game)
  if verbose:
    print_end_of_game_results(game_records, player1, player2)

def print_start_of_game(game):
   print("Starting game")
   print("player 1:", game.player1)
   print("player 2:", game.player2)

def print_turn_record(turn_stats):
    print("Turn number:", turn_stats[0])
    print("Time taken:", round(turn_stats[1], 6))
    print("Nodes visited:", turn_stats[2])
    print("Player color: ", turn_stats[3])
    print(f"Score: {turn_stats[4]} => {sum(turn_stats[4][0]) - sum(turn_stats[4][1])}")
    print("\n")

def print_end_of_game_results(game_records, player1, player2):
    print("Game over")
    print("Final score:", game_records[-1][4], "=>", sum(game_records[-1][4][0]) - sum(game_records[-1][4][1]))
    print("Player 1:", player1.name, "\ttime taken:", round(sum([record[1] for record in game_records if record[3] == 1]), 6), "\tnodes visited:", sum([record[2] for record in game_records if record[3] == 1]))
    print("Player 2:", player2.name, "\ttime taken:", round(sum([record[1] for record in game_records if record[3] == 2]), 6), "\tnodes visited:", sum([record[2] for record in game_records if record[3] == 2]))
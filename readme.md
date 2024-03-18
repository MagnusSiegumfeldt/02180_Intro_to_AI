# Taiji
This project contains a Taiji engine as well as a four different AI players.

## AI models
The iterative development of our AI is shown by the different players found in the source code. The ```MinimaxArea``` player is our simplest version while the ```MinimaxAlphaBetaHashingAdvanced``` has been extended and improved.

## Setting up and executing the code
You need [pygame](https://www.pygame.org/news) to run our implementation and play against the AI yourself. Install this by
```
pip install -r requirements.txt
```
Run a GUI window against our AI with
```
python ./src/main.py
```
To have two AIs play a match can be launched by
```
python ./src/testrunner.py <id_white> <id_black> <depth_white> <depth_black>
```
where the ids are as follows: 
| Id | Search Method| State Hashing | Advanced Board Evaluation              |
|----|-----------|-|---------------|
| 0  | Minimax | No | No
| 1  | $\alpha\beta$-pruning| No| No                |
| 2  | $\alpha\beta$-pruning| Yes| No
| 3  | $\alpha\beta$-pruning| Yes| Yes

e.g. run 
```
python ./src/testrunner.py 3 0 4 2
```
to execute a game between our most advanced AI with search depth 4 playing as white and our simplest AI with search depth 2 playing as black. 

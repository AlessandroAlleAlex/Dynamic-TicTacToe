# Dynamic TicTacToe Game

Both the board size and the win checks are dynamic.

The first player will always be '1' and the second player will be '2'.

The alternation between the players is achieved through the itertool library in python:

```
import itertools

player_choise = itertools.cycle([1, 2])
current_player = next(player_choise)
print(f'Current Player: {current_player}')
```

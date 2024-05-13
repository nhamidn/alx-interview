# 0x0A. Prime Game

## Project Description
In this project, you'll delve into a game-theoretic problem involving prime numbers, strategic game play, and optimization algorithms. Maria and Ben play a game where they alternately pick prime numbers from a set of consecutive integers and remove those numbers and their multiples. The player unable to make a move loses.

### Concepts Needed
- **Prime Numbers**:
  - Understanding of what prime numbers are and efficient algorithms for identifying them, like the Sieve of Eratosthenes.
- **Game Theory**:
  - Basic principles of games where players take turns, with an emphasis on optimal play and understanding win conditions.
- **Dynamic Programming/Memoization**:
  - Using previous results to make future calculations faster to optimize the solution for multiple game rounds.
- **Python Programming**:
  - Implementing loops, conditional statements, and managing lists to track game state.

### Resources
- [Prime Numbers Introduction](https://www.khanacademy.org/math)
- [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
- [Game Theory Introduction](https://www.investopedia.com/terms/g/gametheory.asp)
- [Dynamic Programming with Python Examples](https://www.realpython.com/python-dynamic-programming/)
- [Python Official Documentation on Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Requirements
- **Environment**: Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **Editors**: vi, vim, emacs
- **Documentation**: A README.md file is mandatory
- **Code Style**: PEP 8 style (version 1.7.x)
- **Execution**: All files must be executable with the first line `#!/usr/bin/python3`
- **Restrictions**: No external packages are allowed to be imported

### Task: Prime Game
**Function Prototype**: `def isWinner(x, nums)`

- **Parameters**:
  - `x`: number of rounds
  - `nums`: an array of `n` representing the largest number in each round's set
- **Returns**: Name of the player that won the most rounds or `None` if the winner cannot be determined
- **Constraints**: Assume `n` and `x` will not be larger than 10000

#### Example Gameplay:
```plaintext
x = 3, nums = [4, 5, 1]
First round: n = 4
Maria picks 2, removes 2 and 4 -> remaining [1, 3]
Ben picks 3, removes 3 -> remaining [1]
Ben wins (no primes left for Maria).

Second round: n = 5
Maria picks 2, removes 2 and 4 -> remaining [1, 3, 5]
Ben picks 3, removes 3 -> remaining [1, 5]
Maria picks 5, removes 5 -> remaining [1]
Maria wins (no primes left for Ben).

Third round: n = 1
Ben wins (no primes for Maria to pick).

Result: Ben has the most wins.

```
#!/usr/bin/python3
"""
Main file for testing
"""

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

#### Output:
```
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
```

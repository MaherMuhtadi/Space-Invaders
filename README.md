<div align="center">

# Space Invaders

![image](https://user-images.githubusercontent.com/99841502/209762911-6c413560-cda7-4ede-bf16-474dfe3a68d5.png)

</div>

## Description
This is a simple version of the Space Invaders game programmed with Python using the [PyGame](https://www.pygame.org/docs/) library.

PyGame is a set of Python modules that simplifies 2-D game development for beginners. I used this project as a means to explore the capabilities of this library and learn the basics of game development. As an experimental project, I did not attempt to modularise my code.

### Features
1. The player can move sideways on the screen using the <kbd><</kbd> and <kbd>></kbd> keys.
2. Player can shoot lasers at enemies using the <kbd>space bar</kbd>.
3. To avoid spamming laser blasts, lasers can only be shot if there is no previous projectile on screen.
4. The game can be paused and resumed using the <kbd>esc</kbd> key.
5. The game follows a linear rise in difficulty as the player's score increases. For simplicity, this is done by the increasing speed of the game entities.
6. The game is over once an enemy sprite collides with the player's sprite.
7. The player has the option to replay the game after it is over by pressing the <kbd>enter</kbd> key.
8. The game can track and display the player's current score and the highest score so far. The high score is updated in an external text file every time the game ends.

## Installation

### Prerequisites
1. Download and install the latest version of [Python](https://www.python.org/downloads/) that is compatible with [PyGame](https://www.pygame.org/wiki/GettingStarted).
2. Check if python is properly installed along with its package installer using the following commands in your terminal:
```
$ python --version
$ python -m pip --version
```
3. If the Python package installer, pip, is not installed, get it installed using the [pip documentation](https://pip.pypa.io/en/stable/getting-started/).
4. Install the PyGame module by running the following command in your terminal:

    `pip install pygame`

### Usage
1. Download the repository as a ZIP or [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repository to your local device.
2. On your terminal, change directory to the repository folder using the `cd` command.
3. Run the `main.py` file using the command:

    `python main.py`
---
Last Updated: January 09, 2023
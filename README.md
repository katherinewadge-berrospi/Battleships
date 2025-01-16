# BATTLESHIPS

Welcome,
BattleShips is a terminal-based Python game where you compete against an opponent to sink their hidden ships on a grid. This game is a fun way to practice Python programming concepts like loops, functions, and random number generation.

Project 3 for the Code Institute. Please visit the live site [here](https://battleships-kwb-853aa1c83842.herokuapp.com/).

Contents:
1. [Introduction](#introduction)
2. [Features](#features)
3. [Testing](#testing)
4. [Deployment](#deployment)
5. [Future](#future)
6. [Credits](#credits) 


## Introduction

### How to play
1. The game is played on a grid where opponent's ships are hidden.
2. Players and the opponent (computer) take turns targeting positions by marking co-ordinates.
3. Points are awarded as follows:
    - Hit ("!"): +3 points
    - Miss ("X"): -1 point
4. The goal is to sink all the opponent's ships before they sink yours.
5. Ships have each other's backs and come in pairs (2 adjacent tiles, horizontally or vertically).
6. You can choose the board size (from 5x5 to 10x10).
7. The number of ships is double the smaller dimension of the board.

### Mock Up
This is how the programme appears on various devices.

![MockUp](assets/img/battleships-mockup.jpg)


## Features

### Welcome screen:
A magenta "welcome to battleships" and a white name entry message are the first messages the user sees as soon as they run the program. Once entered, the rules of the game (also in magenta) are displayed for users to uderstand all the rules to this variation of Battleships. This is then followed by a prompt for users to choose their board size where they can choose the number of rows and columns independently from 5 to 10. In the rules they were advised that the smaller the board, the easier the game.

![WelcomeScreen](assets/img/battleships-startup.jpg)

### Turns
The turns are highlighted in a magenta colour that continues the theme from the previous messages. The function display_boards() in run.py is responsible for the turns increasing by 1 each round. It displays how many ships each player has left on their boards, an easy way for the user to track their progress, followed by the player's board being printed, then the opponent's. "O"'s represent the empty grid spaces, "#" represents the player's ships whilst the opponent's are hidden. The score board is then displayed and starts the game with 0 points each. Finally, the player gets to go first and choose their first target.

![PlayersTurn](assets/img/battleships-turn-one.png)

Once the player has selected their target row and column, they are told whether they got a hit or a miss. This is immediately followed by the opponet's turn which is automated and selects a random co-ordinate but it cannot be one that's already been selected. Lastly, players are told whether their opponent hit or missed on of their ships before going to the next round.

![OpponentsTurn](assets/img/battleships-opponents-turn.jpg)

### End Game
The number of turns in a game is not limited, the only way a winner is declared is by sinking all the opponents ships. When a player wins the game they are greeted with a congratulations message in green and the player's name at the end to make it more personal.

![Winner](assets/img/battleships-winner.jpg)

However, if the player cannot sink all the opponent's ships in time, they must be declared the loser. They are then given a message in red stating that they lost the game. Lastly, no matter the outcome, win or lose, players are given their final scores.

![Loser](assets/img/battleships-loser.jpg)


## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

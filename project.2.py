#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


import random
moves = ['rock', 'paper', 'scissors']
play_style = ["random", "reflect", "rocker", "cycle"]
"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.opponent_move = "paper"
        self.score = 0  # for keeping score

    def move(self):
        return 'rock'  # player that always plays 'rock'.

    def learn(self, my_move, their_move):
        self.my_last_move = my_move
        self.opponent_move = their_move


class randomPlayer(Player):
    def move(self):
        return random.choice(moves)  # player play random


# player that asks the human user what move to make.
class humanPlayer(Player):
    def move(self):
        humanPlayerMove = ''
        while humanPlayerMove not in moves:
            humanPlayerMove = input("Enter a move: ").lower()
            if humanPlayerMove == "q":
                exit()

        return humanPlayerMove  # player play by the user.


class ReflectPlayer(Player):
    def move(self):
        # player that remembers what move the opponent played last round, and plays that move this round.
        return self.opponent_move


# player that remembers what move it played last round, and cycles through the different move
class CyclePlayer(Player):
    def move(self):
        if self.opponent_move == "rock":
            return "paper"
        elif self.opponent_move == "paper":
            return "scissors"
        elif self.opponent_move == "scissors":
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1.score += 1  # if player one won add score +1
            print("Player 1 won this round")
        elif beats(move2, move1):
            self.p2.score += 1  # if player two won add score +1
            print("player 2 won this round")
        else:
            print("Draw")  # this mean two player play same thing

        print(f"Player 1: {self.p1.score}  Player 2: {self.p2.score}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

        if self.p1.score > self.p2.score:
            print("the player 1 is won the game")
        elif self.p2.score > self.p1.score:
            print("the Player 2 is won the game")
        else:
            print("Draw")


if __name__ == '__main__':
    userinput = ""
    while userinput not in play_style:
        # take input from user to select any player to play with
        userinput = input("select a player to play againts: ").lower()
        if userinput == "q":
            exit()

    if userinput == "random":
        game = Game(humanPlayer(), randomPlayer())
    elif userinput == "reflect":
        game = Game(humanPlayer(), ReflectPlayer())
    elif userinput == "cycle":
        game = Game(humanPlayer(), CyclePlayer())
    elif userinput == "rocker":
        game = Game(humanPlayer(), Player())

    game.play_game()

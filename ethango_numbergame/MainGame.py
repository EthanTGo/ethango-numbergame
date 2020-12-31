from Error import ZeroOrLessError
from Player import Player
import random

class Game:

    def __init__(self):

        """ Basic game board setup for the game.

        Attributes:
            num_players (int): keeps track of number of players in the game
            list_players (list): list of Players object that the game will store and iterate over
            counter (int): keeps tracks of which player is playing at the time
            number (int): The number the player will need to guess
        """
        while True:
            try:
                num_players = int(input("Enter the number of players: "))
                if(num_players > 0):
                    self.num_players = num_players
                    self.list_players = self.create_players(self.num_players)
                    self.counter = 0
                    self.number = self.create_guess()
                    break
                else:
                    raise ZeroOrLessError
            except ZeroOrLessError:
                print("You can only enter a number greater than 0")
                print()
    




    def create_players(self, num_players):
        """
            This function creates and initialize the list of players for the gmae object

            Input: 
                num_players: The number of players to create

            Output:
                list_players: A list of players
        """
        list_players = []
        for _ in range(num_players):
            name = input("Enter your name")
            list_players.append(Player(name))
        self.list_players = list_players
        return list_players

    def create_guess(self):
        """
            This function makes the number that the player would have to guess

            Input:
                None

            Output:
                number (int): The number that the player will need to guess
        """
        return random.randint(0,100)

    def next_turn(self):
        """
            Function that progresses the game to the next player. It looks at counter to see which playuer is currently playing.
            It then asks the player to guess the number, if the number is correct he gets point, 
            otherwise game returns (Higher or Lower) prompt as hint.

            Input:
                None

            Output:
                None
        """
        current_player = self.list_players[self.counter]
        guess = int(input("Enter your number player {player_num}".format(player_num = self.counter + 1)))
        if(guess == self.number):
            print("Congratulations! You guessed the correct number. We will now initialize a different number")
        else:
            if(guess > self.number):
                print("Your guess was incorrect, it is lower")
            elif(guess < self.number):
                print("Your guess was incorrect, it is higher")


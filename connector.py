"""Module that connects whole functionality of the game."""
from game import game
from village import return_to_village


def run_game_again(hero):
    """Functions that run game scene."""
    game(hero)


def run_village_stage(hero):
    """Function that runs village scene."""
    return_to_village(hero)

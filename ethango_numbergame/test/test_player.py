import sys

# This is used to look for the file we will import
sys.path.insert(1, '/Users/ethango/Desktop/ethango-numbergame/ethango_numbergame')

# Requires code above for following import to be doable
from Player import Player

'''
Test several components of the Player class to make sure everything is as expected
'''

def test_player_0():
    player = Player('Ethan')
    assert(player.name == 'Ethan')
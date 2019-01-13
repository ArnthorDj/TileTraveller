
class Tile():

    def __init__(self, west_wall = False, south_wall = False, coins = 0):
        self.west_wall = west_wall
        self.south_wall = south_wall
        self.coins = coins
    
    def areCoins(self):
        if(self.coins > 0):
            return True
        return False

    def getCoins(self):
        if self.coins > 0:
            self.coins -= 1
            return 1
        return 0
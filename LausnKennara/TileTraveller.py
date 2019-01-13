#LAUSN KENNARA

from Position import Position
from Grid import Grid

class TileTraveller():

    def __init__(self):
        self.points = 0
        self.position = Position(0,0)
        self.grid = Grid(4,3)

    def playGame(self):
        print("Enert Q at anytime to quit")
        while True:
            if(self.grid.isInEnd(self.position)):

                print("\nYou have Won!\n\n")
                self.position = Position(0,0)
                self.point = 0
                self.grid = Grid(4,3)
                
            print(self.grid.getPossibilities(self.position))
            input_str = input("Enter your choice: ").lower()
            if(input_str == "q"):
                exit()
            elif(input_str == "g"):
                got_coins = self.grid.getCoins(self.position)
                self.points += got_coins
                if got_coins > 0:
                    print("You found " + str(got_coins) + " coins!")
                else:
                    print("There are no coins!")
            else:
                print(self.grid.move(self.position, input_str))


tile_traveller = TileTraveller()
tile_traveller.playGame()
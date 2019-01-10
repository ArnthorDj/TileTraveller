NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"
#----------------------------------------------------------------------------------------------------------------------------------
class Game():
    def __init__(self):
        self.__victory_position = [3,3]
        self.__player = Player()
        self.__tile_list = self.createTileList(3,3)
        self.__grid = Grid(self.__tile_list)
        self.main()

    def getVictoryPosition(self):
        return self.__victory_position

    def createTileList(self, height, width):
        tile_list = [
                    [[Tile([0,1,1,1])],[Tile([0,0,0,1])],[Tile([1,0,0,1])]]
                    [[Tile([0,1,1,1])],[Tile([1,1,0,0])],[Tile([1,0,1,0])]]
                    [[Tile([0,1,1,1])],[Tile([0,1,0,1])],[Tile([1,1,0,0])]]
                    ]
        return tile_list

    def Victory(self):
        victory_position = self.getVictoryPosition()
        return self.__player.position[0] == victory_position[0] and self.__player.position[1] == victory_position[1]

    def displayText():

    def main(self):
        while(not self.Victory()):
            
#----------------------------------------------------------------------------------------------------------------------------------

class Player():
    def __init__(self):
        self.__position = [0,0]
#----------------------------------------------------------------------------------------------------------------------------------
class Grid():
    def __init__(self, tile_list):
        self.__tile_instance_list = tile_list
        
#----------------------------------------------------------------------------------------------------------------------------------

class Tile():
    def __init__(self, wall_list):
        self.__wall_list = wall_list
        self.__valid_dir = self.getValidDir()
    
    def getWallList(self):
        return self.__wall_list
    
    def getValidDir(self):
        wall_list = self.getWallList()
        valid_dir = []
        if(wall_list[0] == 0):
            valid_dir.append(NORTH)
        if(wall_list[1] == 0):
            valid_dir.append(EAST)
        if(wall_list[2] == 0):
            valid_dir.append(SOUTH)
        if(wall_list[3] == 0):
            valid_dir.append(WEST)
        return valid_dir
#----------------------------------------------------------------------------------------------------------------------------------
game = Game()
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
    def getPlayer(self):
        return self.__player
    def getGrid(self):
        return self.__grid

    def createTileList(self, height, width):
        tile_list = [
                    [[Tile([0,1,1,1])],[Tile([0,0,0,1])],[Tile([1,0,0,1])]],
                    [[Tile([0,1,1,1])],[Tile([1,1,0,0])],[Tile([1,0,1,0])]],
                    [[Tile([0,1,1,1])],[Tile([0,1,0,1])],[Tile([1,1,0,0])]]
                    ]
        return tile_list

    def Victory(self):
        victory_position = self.getVictoryPosition()
        player_pos = self.getPlayer().getPlayerPosition()
        return player_pos[0] == victory_position[0] and player_pos[1] == victory_position[1]

    def getDisplayText(self):
        player_position = self.getPlayer().getPlayerPosition()
        tile = self.getGrid().searchGrid(player_position)
        return tile.getValidDir()

    def displayText(self, valid_dir):
        print(valid_dir)
        print("This is the text.")

    def main(self):
        while(not self.Victory()):
            #Displays the valid diractions
            self.displayText(self.getDisplayText())
            break
            
#----------------------------------------------------------------------------------------------------------------------------------

class Player():
    def __init__(self):
        self.__position = [0,0]

    def getPlayerPosition(self):
        return self.__position
    
    def setPlayerPosition(self, new_Position):
        self.__position = new_Position
#----------------------------------------------------------------------------------------------------------------------------------
class Grid():
    def __init__(self, tile_list):
        self.__tile_list = tile_list
    
    def getTileList(self):
        return self.__tile_list

    def searchGrid(self, tile_position):
        tile_list = self.getTileList()
        return tile_list[0][tile_position[0]][tile_position[1]]
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

    def __str__(self):
        wall_list = self.getWallList()
        return "{}-{}-{}-{}".format(wall_list[0], wall_list[1], wall_list[2], wall_list[3])
#----------------------------------------------------------------------------------------------------------------------------------
game = Game()
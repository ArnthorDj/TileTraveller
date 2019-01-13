
from Tile import Tile
from Position import Position

class Grid():

    def __init__(self, width = 3, height = 3):
        self.height = height
        self.width = width
        self.tiles = None
        self.buildMaze()
    
    def buildMaze(self):
        self.tiles = []
        for i in range(self.width):
            self.tiles.append([])
            for _ in range(self.height):
                self.tiles[i].append(Tile())
                     
        self.tiles[1][0].west_wall = True
        self.tiles[1][2].south_wall = True
        self.tiles[2][1].west_wall = True
        self.tiles[2][0].west_wall = True

        self.tiles[2][2].south_wall = True
        self.tiles[3][1].south_wall = True

        self.tiles[0][1].coins = 1
        self.tiles[1][0].coins = 3
    
    def can_go(self, position, input_str):
        if(input_str == "N"):
            if(position.y >= 0 and position.y + 1 < self.height 
            and position.x >= 0 and position.x < self.width 
            and self.tiles[position.x][position.y + 1].south_wall == False ):
                return True
            return False
        
        elif(input_str == "S"):
            if(position.y > 0 and position.y < self.height 
            and position.x >= 0 and position.x < self.width 
            and self.tiles[position.x][position.y].south_wall == False ):
                return True
            return False
        
        elif(input_str == "E"):
            if(position.y >= 0 and position.y < self.height 
            and position.x >= 0 and position.x + 1 < self.width 
            and self.tiles[position.x + 1][position.y].west_wall == False ):
                return True
            return False

        elif(input_str == "W"):
            if(position.y >= 0 and position.y < self.height 
            and position.x > 0 and position.x < self.width 
            and self.tiles[position.x][position.y].west_wall == False ):
                return True
            return False
        return False

    def move(self, position, input_str):
        if(input_str.lower() == "n"):
            if(self.can_go(position, "N")):
                position.y += 1
                return "Moved North!"
            return "Can't Move North!"
        
        elif(input_str.lower() == "s"):
            if(self.can_go(position, "S")):
                position.y -= 1
                return "Moved South!"
            return "Can't Move South!"
        
        elif(input_str.lower() == "e"):
            if(self.can_go(position, "E")):
                position.x += 1
                return "Moved East!"
            return "Can't Move East!"

        elif(input_str.lower() == "w"):
            if(self.can_go(position, "W")):
                position.x -= 1
                return "Moved West!"
            return "Can't Move West!"

        return "Invalid input!"
    
    def getCoins(self, position):
        return self.tiles[position.x][position.y].getCoins()
        

    def getPossibilities(self, position):
        ret_str = "possibilities are:"
        if(self.can_go(position, "N")):
            ret_str += "\nN: go north"
        if(self.can_go(position, "E")):
            ret_str += "\nE: go east"
        if(self.can_go(position, "S")):
            ret_str += "\nS: go south"
        if(self.can_go(position, "W")):
            ret_str += "\nW: go west"

        if(self.tiles[position.x][position.y].areCoins()):
            ret_str += "\nG: Get Coins!"

        return ret_str
    
    def isInEnd(self, position):
        return position.x == self.width -1 and position.y == 0
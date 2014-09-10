"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result_line =[0]*len(line)
    merged = False
    for dummy_i in range(len(line)):
       if line[dummy_i] != 0:
            idk = result_line.index(0)
            if idk ==0:
                result_line[idk] = line[dummy_i]
            elif result_line[idk-1]==line[dummy_i] and merged == False:
                result_line[idk-1] = 2*line[dummy_i]
                merged = True
            else:
                result_line[idk] = line[dummy_i]
                merged = False
    return result_line
   
class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.start_board = self.reset()
        #creates the dictionary to be used in the move method
        up_list = []
        down_list = []
        left_list = []
        right_list = []
        for idi in range(grid_width):
            up_list.append((0,idi))
            down_list.append((grid_height-1,idi))
        for idj in range(grid_height):
            left_list.append((idj,0))
            right_list.append((idj,grid_width-1))
        self.init_dict = {UP:up_list, DOWN:down_list, LEFT:left_list, RIGHT:right_list}
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.cells = [ [0 for _row in range(self.grid_width)] for _col in range(self.grid_height) ]
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        for tile_loc in self.init_dict[direction]:
            if (direction == UP) or (direction == DOWN):
                temp_list =[]
                for idc in range(self.grid_height):
                    result = self.cells[tile_loc[0] + idc*OFFSETS[direction][0]][tile_loc[1] + idc*OFFSETS[direction][1]]
                    temp_list.append(result)
                moved = merge(temp_list)
                for idc in range(self.grid_height):
                    self.set_tile(tile_loc[0] + idc*OFFSETS[direction][0], tile_loc[1] + idc*OFFSETS[direction][1], moved[idc])
             
                
            elif (direction == LEFT) or (direction == RIGHT):
                temp_list =[]
                for idr in range(self.grid_width):
                    result = self.cells[tile_loc[0] + idr*OFFSETS[direction][0]][tile_loc[1] + idr*OFFSETS[direction][1]]
                    temp_list.append(result)
                moved = merge(temp_list)
                for idr in range(self.grid_height):
                    self.set_tile(tile_loc[0] + idr*OFFSETS[direction][0], tile_loc[1] + idr*OFFSETS[direction][1], moved[idr])
        self.new_tile()
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # locate coordinates of all empty cells.
        location = []
        for idi in range(0,self.grid_width):
            for idj in range(0, self.grid_height):
                if self.cells[idi][idj] == 0:
                     location.append([idi,idj])
           
        #assign appropriate numbers to an empty location
        value = random.choice([2,2,2,2,2,2,2,2,2,4])
        if location != []:
            select_key = random.choice(location)
            self.set_tile(select_key[0], select_key[1], value)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """ 
        return self.cells[row][col]
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


# dungeonGen.py is used when we want to turn a perfect maze into a 'dungeon'. Before we do that though, we need to know what we define a dungeon as. We want it to have winding passages that intersect with wide open rooms and to also not be perfect, there should be ways of looping back onto yourself. 

from random import randint

def createGaps(board, size):
  deltaX = [0, 1, 0, -1] # used to loop through movements in the x-axis
  deltaY = [1, 0, -1, 0] # used to loop through movements in the y-axis
  # createGaps(board, size) is used to convert a perfect maze into a wide open dungeon without rooms. It doess this by importing the current board(board) and size(the length of one side of the maze) and then loops through the entire maze, filling in any dead ends. It then returns the updated 'maze' which should have large gaps in it. 
  for i in range(size-1): # loop through every line
    for n in range(size-1): # loop through every character in each line
      amountOfPaths = 0 # amountOfPaths is used to keep track of if it's a dead end or not. If there is 1 potential path then it's a dead end.
      if board[i][n] == " ": # if we come across a path...
       for k in range(4): # ...then loop through every possible direction...
          try: # try is used as we expect index errors here. As the program checks every potential movement, if it's at an edge the a index error is guaranteed.
            if board[i+deltaY[k]][n+deltaX[k]] == " ": # ...and if one of those movements is valid...
              amountOfPaths += 1 # ...then increment amountOfPaths.
          except IndexError: # if we run into the predicted error...
            pass # do nothing and just continue the program.
      if amountOfPaths == 1: # if the found spot is a dead end...
        board[i][n] = "-" # ...fill it in with a wall.
  return board # once the entire board has been looped through, return it. 
  
def imperfectify(board, size): #takes the maze and adds in gaps between paths, used to allow looping back onto yourself.
  percentage = 5
  for i in range(size-1):
    for n in range(size-1):
      if board[i][n] == "-":
        validDirections = [False, False] # validDirections[0] used to see if there is paths to both sides on the x-axis. validDirections[1] is the same for the y-axis
        try:
          if board[i+1][n] == " " and board[i-1][n] == " ":
            validDirections[0] = True
          if board[i][n+1] == " " and board[i][n-1] == " ":
            validDirections[1] = True
        except IndexError:
          pass
        if validDirections[0] == True and validDirections[1] == False:
          if randint(0,100) <= percentage:
            board[i][n] = " "
        elif validDirections[0] == False and validDirections[1] == True:
          if randint(0, 100) <= percentage:
            board[i][n] = " "
  return board

class room:
  def __init__(self):
    self.minSize = 2 # minimum size of a room, set to 2 to ensure rooms aren't just long corridors
    self.maxSize = 10 # maximum size of a room, set to 10 to ensure rooms aren't too big
    self.width = randint(self.minSize, self.maxSize) # finds random with within range
    self.height = randint(self.minSize ,self.maxSize) # finds random height within range
    self.area = self.height * self.width # finds the area of the room

  
  def findValidPlacement(self, board, size):
    ''' 
    findValidPlacement(self, board, size) will find if a room could potentially fit in a posistion. It does this by looping through each posistion
    in the board and them attempting to fit the room in there. It does so by verifying that every spot that the room could fill 
    is a wall ('-'). If it finds a wall in posistion it's trying to verify, it will add 1 onto 'counter'. If at the end of the 
    loop, counter is equal to the area of the room, then we have found a valid posistion for the room to be placed in. It will 
    then return 'roomData' which is an array that countains:
    [y-coordanite of the room, x-coordanite of the room, width of the room, height of the room]
    
    If the room posistion is not valid however, the program will continue onto the next posistion in the board to verify. If 
    it turns out that no posistion in the board is valid, then roomData will be returned. This time though, it will be a False
    value to signify that the room cannot fit into this dundgeon.
    '''
    for k in range(size): # for every line in the board
      for z in range(size): # for every posistion in the board
        if board[k][z] == "-": # if the posistion is a wall...
          counter = 0 # begin to try and find if this could be a valid posistion
          for i in range(self.height): # for the height of the room...
            for n in range(self.width): # for the widht of the room...
              try: # try/except is used as if the room posistion being tested is near the edge of the board then IndexErrors are to be expected.
                if board[k+i][z+n] == "-": # if the posistion being tested is a wall...
                  counter += 1
                else: # if it's not a wall... 
                  break
              except IndexError:  # and if it dosen't exist...
                break
          if counter == self.area:
            roomData = [k, z, self.width, self.height] # k is the y coord of the room. z is the x coord of the room
            return roomData 
    return False
    
  def placeRoom(self, pos, board):
    for i in range(self.height-2):
      for n in range(self.width-2):
          board[pos[0] + i + 1][pos[1] + n + 1] = " " # for every part of the room, remove a wall. '+ 1' is to ensure there's walls around the room
    return board
  
  def connectRoom(self, pos, board):
    possibleConnections = [[],[],[],[]]
    for i in range(self.width-2):
      if board[pos[0] - 1][pos[1] + i + 1] == " " and board[pos[0] + 1][pos[1] + i + 1] == " ":
        possibleConnections[0].append(str(pos[0])+','+str(pos[1] + i +1))
      # bottom connections
      if board[pos[0] + self.height - 1][pos[1] + i + 1] == " " and board[pos[0] + self.height + 1][pos[1] + i + 1] == " ":
        possibleConnections[1].append(str(pos[0] + self.height) + ',' + str(pos[1] + i + 1))
    for i in range(self.height-2):
      #left connections
      if board[pos[0] + i + 1][pos[1] - 1] == " " and board[pos[0] + i + 1][pos[1] + 1] == " ":
        possibleConnections[2].append(str(pos[0] + i + 1)+','+str(pos[1]))
      #right connections
      if board[pos[0] + i + 1][pos[1] - 1 + self.width] == ' ' and board[pos[0] + i + 1][pos[1] + 1 + self.width] == ' ':
        possibleConnections[3].append(str(pos[0] + i + 1)+','+str(pos[1]+self.width))
    for i in range(4):
      try:
        DoorCoord = possibleConnections[i][randint(0,len(possibleConnections[i]))].split(',')
        board[int(DoorCoord[0])][int(DoorCoord[1])] = " "
      except IndexError:
        pass
    return board
# -- Modules --

import random


# -- global variabes / constants--
yMovementAmount = [2, 0, -2, 0] # used both in createMaze() and validateDirections() to loop through movements in the Y-Axis 
xMovementAmount = [0, 2, 0, -2] # identical to yMovementAmount but used for the X-Axis


# -- functions --

# prints the current layout of variable 'board'
def printBoard(board): 
  text = "" # sets up a temp variable called 'text', used to store the maze in it's entiraty in string format
  for line in board:  # for every line in the board...
    for i in range(len(line)): # it will iterate through every character in that line
      if line[i] == "-":
        text = text + "[]"
      else:
        text = text + "  "
    text = text + "\n" # once the line is over add on a line break
  print(text) 

# takes a 2d array where all values are set to '-' and then turns it into a maze by using a random depth-first search
def createMaze(board, x, y): 
  start = [-1, -1]  # initilises the start of the maze
  start[0], start[1] = random.randrange(1, y-1, 2), random.randrange(1, x-1, 2) # finds random odd start point. It's important that both the start point and diamaters of the maze are odd as it restricts the program from designating edges as possible paths. 
  board[start[0]][start[1]] = " " # sets the start to ' '
  pathOfCursor = [] # stack used to store where the cursor has been. The program will loop through the maze, creating random paths, all while adding onto 'pathOfCursor' with every iteration. When it encounters a dead end, the top value will be popped off and the next position will be validated with a potential new path or again be popped off. When this stack is empty, it means that the maze is complete.
  pathOfCursor.append(start)
  while True: # we want to have an infinite loop as we need the program to continue running through the maze, no matter the size. This loop will be broken on line 35
    if len(pathOfCursor) == 0: # if the stack is empty...
      print("Finished maze gen...") # ...then the maze is finished and...
      return board # ...return the finished maze and break the loop
    validMovements = validateDirections(pathOfCursor[len(pathOfCursor)-1], board) # sets validMovements to whatever validateDirections returns. Passes in the top value of the stack and the board
    if not any(validMovements): # if there are no possible movements, for example a dead end...
      pathOfCursor.pop() # then pop the top value of the stack and search for another possible direction
    else: # if there are possible movements...
      chosenDir = random.randrange(4) # choose a random direction. This is done as sometimes, not all of the directions are valid. In this situation, DundGen chooses a random direction and sees if it is valid according to validMovements
      while validMovements[chosenDir] == False: # loop until chosenDir is a valid movement according to validMovements[chosenDir]
        chosenDir = random.randrange(4)
      board[pathOfCursor[len(pathOfCursor)-1][0] + yMovementAmount[chosenDir]][pathOfCursor[len(pathOfCursor)-1][1] + xMovementAmount[chosenDir]] = " " # sets the position two spaces away from the cursor in the chosen direction to ' '. 
      board[pathOfCursor[len(pathOfCursor)-1][0] + yMovementAmount[chosenDir] // 2 ][pathOfCursor[len(pathOfCursor)-1][1] + xMovementAmount[chosenDir] // 2 ] = " " # sets the position one space away from the cursor in the chosen direction to ' '.
      pathOfCursor.append([pathOfCursor[len(pathOfCursor)-1][0] + yMovementAmount[chosenDir], pathOfCursor[len(pathOfCursor)-1][1] + xMovementAmount[chosenDir]]) # pushes the position two spaces away from the cursor in the chosen direction onto pathOfCursor. This will become the new cursor.

def validateDirections(curPos, board): # identifies directions around the 'curPos' (current position) that are valid
  validMovements = [False, False, False, False] # used to store if movement in a direction is possible, validMovements[0] is down, validMovements[1] is right, validMovements[2] is up and validMovements[3] is downp
  for i in range(4): # for every movement...
    try:
      if board[curPos[0] + yMovementAmount[i]][curPos[1] + xMovementAmount[i]] == "-" and curPos[0] + yMovementAmount[i] > 0 and curPos[1] + xMovementAmount[i] > 0: # check to make sure the direction is valid and...
        validMovements[i] = True # ...if it's valid then set the current direction being validated to True.
    except IndexError: # if it's not valid, expect an Index Error and...
      pass #... do nothing! It's already been set to false, so we just need to make sure the program continues on without a hitch.
  return validMovements # Once all 4 directions have been validated, return the list.
  
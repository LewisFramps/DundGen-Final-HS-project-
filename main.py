'''

Welcome to DundGen! This program was created for my Advanced Higher Computing Science project

--<What Is This program?>--
This programs primary function is to create a randomly generated dungeon. Along with this, it also has a menu system, customizable options and the ability to output a .txt and a .bmp file of the dungeon.

--<How does it work?>--
When generation of the dungeon begins, a 2d array is created and filled with "-" in every posistion. This array will be of a size that is set in the option menu. 

Then, the program will run through the 2d array and turn it into a perfect maze by using randomised depth-first search (see http://www.migapro.com/depth-first-search/ for more information).

After the maze has been created, we begin to turn it into a dungeon. I define that as a large area which is filled with twisting corridors, interconnected rooms and looping paths. To create this, we take the perfect maze and begin to fill in dead ends. This results in long twisting paths and large areas without any paths. We then begin to create randomly sized rooms and start testing to see if the could fit anywhere in the maze. If the room is found to have a valid posistion then it is placed and connected to any surrounding paths/rooms. This process repeats for the amount 'size of maze * 5'.


'''

import mazeGen, dungeonGen, output  # imports other .py files that are used in generation and output. mazeGen is used to turn a blank 2d array into a maze with depth-first. dungeonGen then takes this maze and alters it into more of a playable map. output will then output the results.

# Setup default values
size = [55, 125, 555]  # default choices for sies
sizeChoice = 0  # default choice of size, so the default dungeon will be 55x55
amountOfGaps = 4  # default amount of times the program will loop through the board creating random gaps
imageOutput = True  # default toggle of outputing image file
textOutput = True  # default toggle of outputing text file

print("Welcome to..\n<><> DundGen! <><>\nDundGen is designed to create a customizable dungeon for use in \ntabletop games such as D&D or Pathfinder. It is recommended that you \nexplore the options if this is your first time running DundGen")

def validateInput(userInput, maxChoice, text):  # used to make sure user inputs an integer within acceptable range. Will run at least once so user is shown the text and given chance to input value. userInput is the users input. maxChoice is the number of choices that can be made. text is what prints when an incorrect value is passed in
  if userInput.isdigit():  # if the input is an integer...
      if 0 < int(userInput) <= maxChoice: # and within range...
        return True #...then return true. This breaks out of the function.
  print(text) # If the function gets to this point, then the input is not valid as it would have otherwise returned true. 
  return False

def beginGen(): # starts to Generate dundgeon
    global size, sizeChoice, amountOfGaps, imageOutput, textOutput  # sets previously mentioned variables to global, allowing beginGen to interact with them
    frequencyOfRooms = size[sizeChoice] * 5  # generates the amount of rooms the maze should try and input. * 5 was taken from testing, where it was found to both implement the most valid rooms whilst also being fairly quick to generate

    # setup the board
    board = [["-" for i in range(size[sizeChoice])] for n in range(size[sizeChoice])]  # sets up the variable 'board' as a 2d array. To be used as the base for the dundgeon
    
    # Populate board with a maze
    print("Creating maze...")
    board = mazeGen.createMaze(board, size[sizeChoice], size[sizeChoice]) # calls function createMaze() which is in mazeGen.py. This function will setup the maze using a depth-first algorithm.

    # Fill in dead-ends in maze to create room for rooms.
    print("Creating gaps for rooms...")
    for i in range(size[sizeChoice]): # value chosen as it reliably scales with varying sizes.
      board = dungeonGen.createGaps(board, size[sizeChoice])# This will loop through the maze, backtracking and filling in any dead ends it finds. This results in large areas filled with nothing but walls. These areas are where rooms will be placed.

    # Populate dundgeon with rooms
    print("Adding rooms...")
    for w in range(frequencyOfRooms): # for the generated amount of rooms to try and make...
      newRoom = dungeonGen.room() #...create a new object in the room() class (stored within dungeonGen.py).
      pos = newRoom.findValidPlacement(board, size[sizeChoice]) # runs the findValidPlacement() method. This will find a valid place for the room within the board (valid here means that it will not intersect any other rooms or corridors). pos is then set to the returned array if a valid place is found. pos[0] and pos[1] being y and x coordanites respectively whilst pos[2] and pos[3] being the width and height of the room respectively. If there is no valid placement, then pos will be set to False, resulting in the room being ignored.
      if pos != False: # if a valid place is found...
        board = newRoom.placeRoom(pos,board)  # place the room within board using the newRoom object's method, placeRoom()
        board = newRoom.connectRoom(pos, board)  # connect the new room to other rooms and to the maze by using the connectRoom() method

    # Populate dundgeon with random gaps
    print("Making the dungeon have gaps in walls...")
    for i in range(amountOfGaps):  # for the user defined amount of times, loop through board and add random gaps in walls
      board = dungeonGen.imperfectify(board, size[sizeChoice])  # calls the imperfectify() function which is stored in dungeonGen.py This is used to add random gaps into the maze to give it more of a dungeon-y look
    print("Dungeon Generation Completed!")
    
    # Output now finished dundgeon
    if imageOutput: # if user wants to output the finished dungeon as an image...
        print("Outputting to image file")
        output.createImage(board, size[sizeChoice])  # ...call the createImage() function in output.py
    if textOutput:  # if user wants to output the finished dungeon as text...
        print("Outputing to text file")
        output.createFile(board)  # ...call the createFile() function in output.py
    mazeGen.printBoard(board)
    
    # Bring user back to main menu
    mainMenu(True)  # restart the program, now completed.  # beginGen() is used as the group together the part of the program that is responsible for actually creating the dundgeon and outputing the files.

def optionMenu(): # allows user to alter settings
    def optionMenu_mapSize(): # allows user to edit the size of the end map, gives 3 presest values that are known to work fairly quickly
        global sizeChoice
        print("\n<-------------------------------->\nMaze size is currently set to " + str(size[sizeChoice])+"x"+str(size[sizeChoice]))
        optionChoice = ""
        while not validateInput(optionChoice, 6, "\nPlease select an option for maze size:\n 1 - small (55x55)\n 2 - medium (125x125)\n 3 - large (555x555) ( Warning! Takes a long time to load! ) \n 4 - custom ( Warning ! Not fully supported, can easily break! ) \n 5 - Set to defualt value \n 6 - Exit out to option menu"):
            optionChoice = input("<Maze Size> : ")
        def option1():
            global sizeChoice
            print("Setting Maze Size to small")
            sizeChoice = 0
        def option2():
            global sizeChoice
            print("Setting Maze Size to medium")
            sizeChoice = 1
        def option3():
            global sizeChoice
            print("Setting Maze Size to large")
            sizeChoice = 2
        def option4():
            global sizeChoice
            print("Setting Maze Size to custom value\n!Warning! Not supported fully! Can easily break! Please enter an odd integer for the program to work, otherwise this program will crash!")
            size.append(int(input("<Maze Size> : ")))
            sizeChoice = len(size) - 1
        def option5():
            global sizeChoice
            print("Setting Maze Size to default")
            sizeChoice = 0
        def option6():
            pass
        switcher = {1:option1, 2:option2, 3:option3, 4:option4, 5:option5, 6:option6}
        switcher.get(int(optionChoice))()
        optionMenu()

    def optionMenu_gapFreq(): # allows the user to edit the amounts of holes in the walls of the maze, a high number results in a very open maze while a low number results in basically a map of just corridors
        global amountOfGaps
        print("\n<-------------------------------->\nThe frequency of gaps is currently set to " + str(amountOfGaps) + "\n This value dictates how many times the program will loop through\n the board, creating gaps randomly")
        optionChoice = ""
        while not validateInput(optionChoice, 3, "<-------------------------------->\n 1 - New setting \n 2 - Default Setting(4) \n 3 - Exit to options"):
            optionChoice = input("<Gap Frequency> : ")
        def option1():
            global amountOfGaps
            newValue = input("<Gap Frequency> : ")
            while not validateInput(newValue, 9999999999, "Please enter an integer value"): # should probably get around to changing the 9999 max, do this later
                newValue = input('<Gap Frequency> : ')
            amountOfGaps = int(newValue)
        def option2():
            global amountOfGaps
            amountOfGaps = 4
        def option3():
            pass
        switcherInner = {1:option1, 2:option2, 3:option3}
        switcherInner.get(int(optionChoice))()
        optionMenu()

    def optionMenu_toggleImageOutput(): # toggles the output of an image of the map
        global imageOutput
        print("\n<-------------------------------->\nCurrently, outputting as an image is set to " + str(imageOutput))
        optionChoice = ""
        while not validateInput(optionChoice, 3, "\n 1 - Image Output: True\n 2 - Image Output: False\n 3 - Exit to options"):
            optionChoice = input("<Output Image> : ")
        def option1():
            print("Output as image set to True!")
            global imageOutput
            imageOutput = True # set imageOutput to True
        def option2():
            print("Output as image set to False!")
            global imageOutput
            imageOutput = False # set imageOutput to False
        def option3():
            pass
        switcher = {1:option1, 2:option2, 3:option3}
        switcher.get(int(optionChoice))()
        optionMenu()

    def optionMenu_toggleTextOutput(): # toggles the output of a text version of the map
        global textOutput
        print("\n<-------------------------------->\nCurrently, outputting as a text file is set to " + str(textOutput))
        optionChoice = ""
        while not validateInput(optionChoice, 3, "\n 1 - Text Output: True\n 2 - Text Output: False\n 3 - Exit to options"):
            optionChoice = input("<Output Text> : ")
        def option1():
            print("Output as text set to True!")
            global textOutput
            textOutput = True # set textOutput to True
        def option2():
            print("Output as text set to False!")
            global textOutput
            textOutput = False #  set textOutput to False
        def option3():
            pass

        switcher = {"1":option1, "2":option2, "3":option3}
        switcher.get(optionChoice)()
        optionMenu()

    def optionMenu_mainMenu(): # sends user back to main menu
        mainMenu(False)

    choice = "" # create a blank input that will fail to be valid when validateInput is called with it
    while not validateInput(choice, 5, "\n<-------------------------------->\nPlease select an option:\n 1 - Maze Size \n 2 - Gaps in Dungeon \n 3 - Output image file \n 4 - Output text file \n 5 - back"):
        choice = input("<--> : ")
    switcher = {1:optionMenu_mapSize, 2:optionMenu_gapFreq, 3:optionMenu_toggleImageOutput, 4:optionMenu_toggleTextOutput, 5:optionMenu_mainMenu}
    switcher.get(int(choice))()

 
def mainMenu(completed):# lets users begin dungeon generation, alter settings or quit the program. The 'completed' parameter is a boolean value, if False then the program restarts and runs as normal but if True then the program will restart and run as normal but with with a wee 'thank you for running the program' at the end :)

    def mainMenu_beginGen(): 
      	beginGen() # begin maze generation

    def mainMenu_options():# if user selects option menu...
      optionMenu() # open the option menu

    def mainMenu_quit(): # if user selects to exit the program...
      	print("Thanks for using DudnGen!")
      	quit()	# quit

    if completed: # if the program has been run at least once...
        print("\n\n<><> !FINISHED RUNNING! <><>\nThank you for using DundGen!\n\n")
    switcher = {1:mainMenu_beginGen, 2:mainMenu_options, 3:mainMenu_quit}
    choice = "" 
    while not validateInput(choice, 3, "\n<-------------------------------->\nPlease select an option:\n 1 - Generate dungeon \n 2 - Change dungeon generation options \n 3 - Exit DundGen"):
        choice = input("<--> : ")
    switcher.get(int(choice))()


mainMenu(False) # begin the program without the 'thanks for running'.
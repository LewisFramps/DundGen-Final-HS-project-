from PIL import Image 
# PIL (Python Image Libary)

def createImage(board, size): #using PIL to outport dungeon as an image
  img = Image.new('RGB', (size,size), (154,146,123))  # use the Image.new function from PIL to create new image. This image will be using true colour('RGB'), dimensions of size x size and have a default colour of (154, 146, 123).
  for i in range(size):
      for n in range(size):
          if board[n][i] == " ": # if there is a path in the dungeon...
              img.putpixel((i,n),(230,230,205)) #...fill that pixel with colour (230,230,205)
  img.save(str(size)+".bmp") # save new image as .png
  
def createFile(board):
  f = open('dungeon.txt','w+')
  text = "" # sets up a temp variable called 'text', used to store the maze in it's entiraty in string format
  for line in board:  # for every line in the board...
    for i in range(len(line)): # it will iterate through every character in that line
      if line[i] == "-": # if there is a wall...
        text = text + "[]" # then use [] to show a wall. This was chosen as it's more aesthetically pleasing when viewing a dungeon as a whole
      else: # if there isn't a wall...
        text = text + "  " # use two spaces to show a gap. Again, this was chosen for aesthetic reasons. 
    text = text + "\n" # once the line is over add on a line break
  f.write(text) # write the whole text to a file 
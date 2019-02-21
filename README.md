# DundGen-Final-HS-project-
uploading old project to test out git

Made this just over a year ago as a my Advanced Higher Computing project, was my first real go at a larger scale project. Overall fairly happy with how it turned out, though looking back over it there's defo sections I'd change.

(bellow is taken from first comments of main.py)

 **Welcome to DundGen!**
 
 This program was created for my Advanced Higher Computing Science project
 
 --<What Is This program?>--
 
This programs primary function is to create a randomly generated dungeon. Along with this, it also has a menu system, customizable options and the ability to output a .txt and a .bmp file of the dungeon.

--<How does it work?>--
When generation of the dungeon begins, a 2d array is created and filled with "-" in every posistion. This array will be of a size that is set in the option menu. 
Then, the program will run through the 2d array and turn it into a perfect maze by using randomised depth-first search (see http://www.migapro.com/depth-first-search/ for more information).
After the maze has been created, we begin to turn it into a dungeon. I define that as a large area which is filled with twisting corridors, interconnected rooms and looping paths. To create this, we take the perfect maze and begin to fill in dead ends. This results in long twisting paths and large areas without any paths. We then begin to create randomly sized rooms and start testing to see if the could fit anywhere in the maze. If the room is found to have a valid posistion then it is placed and connected to any surrounding paths/rooms. This process repeats for the amount 'size of maze * 5'.
'''

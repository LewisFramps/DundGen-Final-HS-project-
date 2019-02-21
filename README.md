# **DundGen-Final-HS-project**
uploading old project to test out git

Made this just over a year ago as a my Advanced Higher Computing project, was my first real go at a larger scale project. Overall fairly happy with how it turned out, though looking back over it there's defo sections I'd change.

# Welcome to DundGen!
 
 This program was created for my Advanced Higher Computing Science project
 
What Is This program?
 
>This programs primary function is to create a randomly generated dungeon. Along with this, it also has a menu system, customizable options and the ability to output a .txt and a .bmp file of the dungeon.

How does it work?

>When generation of the dungeon begins, a 2d array is created and filled with "-" in every posistion. This array will be of a size that is set in the option menu. 
Then, the program will run through the 2d array and turn it into a perfect maze by using randomised depth-first search (see http://www.migapro.com/depth-first-search/ for more information).
After the maze has been created, we begin to turn it into a dungeon. I define that as a large area which is filled with twisting corridors, interconnected rooms and looping paths. To create this, we take the perfect maze and begin to fill in dead ends. This results in long twisting paths and large areas without any paths. We then begin to create randomly sized rooms and start testing to see if the could fit anywhere in the maze. If the room is found to have a valid posistion then it is placed and connected to any surrounding paths/rooms. This process repeats for the amount 'size of maze * 5'.

Where can I test it if I don't want to download your nonsense?

>Repl.it was vital to this project. This great resource allowed me to work on this nearly anywhere as long as I had access to a computer, earphones and an internet connection. Try out DundGen without downloading anything here: https://repl.it/@LewisFrampton/AH-Project-Dundgen-1

Where can I find more info on this project?

>Look for 'DundGen - AH Project.pdf' in this project. Contains a writeup of the entire project. I did work on it like 2 years ago so if you've got any questions then just pm me and I'll act like I know what I'm doing. <3


![example dungeon output](https://github.com/LewisFramps/DundGen-Final-HS-project-/blob/master/examplePic.png)

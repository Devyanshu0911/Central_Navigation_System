#To implement the a star alogorithm we will need a few things 

#1)A maze where we can test our algorithm,For this we use a module called pymaze whixh will create a maze of given size with obstacles

#2)priority queue:-in a priority queue each element of the queue is given a priority value and the element with a higher priority
#will be choosen first

#So our alogorithm will choose the cell with the minimum value in the priority queue as well as the f cost value of the cell
#You can use pip install pyamaze to install the pyamaze package

#Let us now look at our algorithm

#pyamaze is a relatively large package and we just need the maze module from it

#we also import the priority queue
from pyamaze import maze,agent,textLabel
from queue import PriorityQueue

#List of major maze commands

#1)maze(no of rows,no of columns):-generates a maze with the given number of rows and columns

#2)maze.CreateMaze():-To create the maze

#3)maze.run():-to get the maze

#4)maxe.rows:-for getting the number of rows in the maze

#5)maze.cols:-for getting the columns of the maze

#6)maze.maze_map:-this is a dictionary where the keys are the cells of the maze and the values are the east,west,north,south with vlaues 
#either 1 or 0 it it is one it means the maze in open in that direction else closed

#7)maze.grid:-it will simply return all the cells in the maze

#Let us now begin the implementation 

#step1:function for calculating the heuteristic value(h value) 

def h(cell1,cell2):
    x1,y1=cell1  #We put the x and y coordinate of cell 1 in x1 and y1

    x2,y2=cell2   #put x and y value of cell 2 in x2 and y2

    return abs(x1-x2)+abs(y1-y2) #return x coord of cell1 - x coord of cell2 + y coord of cell 1 and y coord of cell 2

#step2: begin the a* algorithm

def A_star(m):
    #defining the start cell

    start=(m.rows,m.cols)

    #Next we get our values for the start cell

    #first we define the g score and the f score 

    #The g score will be a dictionary with value initialized as infinity for each cell

    g_score={cell:float("inf") for cell in m.grid}

    g_score[start]=0 #Defining the g score of start cell as 0

    #The f score will also be dictionary with value initialized as inifinity ofr each cell
    f_score={cell:float("inf") for cell in m.grid}

    #The f score is g score + h core

    #Here to get the h cost of a particular cell we pass in the cell and the final cell which is (1,1)
    f_score[start]=h(start,(1,1))

    #Now since we have gotten all our values for the start cell we can start our priority queue and put them init

    open=PriorityQueue()

    open.put((h(start,(1,1)),h(start,(1,1)),start)) #Note:We pass f cost value as h cost itself as it is h cost becoz g cost is zero for start

    #Next we declare another emepty dictionary,we will learn about the use of this a bit later
    apath={}
    #Next we start our loop to examine the other cells
    print(m.maze_map)
    while not open.empty():
        #Next we get our current cell,since we know that the third value in the priority queue is the cell vaalue we can get it through
        #the index
        CurrCell=open.get()[2]

        #If this cell is the goal cell we exit 
        if CurrCell==(1,1):
            break
        
        #Otherwise we look at all four neighbour cells qand calculate their f score and the one with the lowest f score willbe put in the
        # queue

        for d in "ESWN":
            #Next we check for which all direction is the maze open for that cell
            if m.maze_map[CurrCell][d]==True:
                #If the above condition is true then we go to each cell and calculate the f cost

                #we define a separate if condition for each cell in each direction

                if d=='E':
                    #If direction is east then the east cell is in the same row but one right column of the current cell
                    childCell=(CurrCell[0],CurrCell[1]+1)
                
                if d=='W':
                    #If direction is west then the west cell is in the same row but one left column of the current cell
                    childCell=(CurrCell[0],CurrCell[1]-1)

                if d=='N':
                    #If direction is north then the north cell is in the same column but one row above of the current cell
                    childCell=(CurrCell[0]-1,CurrCell[1])

                if d=='S':
                    #If direction is south then the south cell is in the same column but one row below of the current cell
                    childCell=(CurrCell[0]+1,CurrCell[1])
                
                # Next we calculate the g score of this child cell which will be current cell +1 as we are moving one more step away from
                #The start cell
                
                temp_g_score=g_score[CurrCell]+1
                
                #Then we calculate the f score of the child cell
                temp_f_score=temp_g_score+h(childCell,(1,1))

                #then we compare the current f score with the previous f score of the child cell
                if temp_f_score < f_score[childCell]:
                    #Then we update the g score and the f score with this new score

                    g_score[childCell]=temp_g_score
                    f_score[childCell]=temp_f_score

                    #Next we add the values i.e the f score h score and the cell to the queue

                    open.put((temp_f_score,h(childCell,(1,1)),childCell))

                    #Now we use the above declared empty dictionary for storing the current cell as the value and the child cell as the key,
                    #why not the other way aound as multiple childcells can have the same current cell and the value of key in a dictionary
                    #cannot be duplicate

                    apath[childCell]=CurrCell
            
            #Next we declare another dictionary as we will be starting with the end cell in this algo therefore our path cells will be stored 
            #in reverse order,so we would again need to reverse it

    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[apath[cell]]=cell
        cell=apath[cell]
    return fwdPath
        
#Next we create our maze

m=maze(5,5)

m.CreateMaze()

#Next we call our function to get our path

path=A_star(m)

#Next we get the agent class from  the pyamaze module which will navigate through our creted path to test it
#The agent class only takes in one parameter the maze created
a=agent(m,footprints=True)

#Next we call the trace path function to make the agent trace the path

m.tracePath({a:path})

print(m.maze_map)
m.run()





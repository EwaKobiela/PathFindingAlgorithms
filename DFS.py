import cv2
import numpy as np
import collections

def search(node, queue):
    h, v = node[:2] #Find current node in the maze
    if(node == goal):   #Checking if the goal is reached
        print("Goal reached")
        return
    maze[h, v] = "o"    #Marking node as visited

    #Try to move in one of four directions
    if (valid(h, v+1) == True): #right
        node = [h, v+1]
        queue.append(node)
        search(node, queue)
    elif (valid(h+1, v) == True): #up
        node = [h+1, v]
        queue.append(node)
        search(node, queue)
    elif (valid(h, v-1) == True): #left
        node = [h, v-1]
        queue.append(node)
        search(node, queue)
    elif (valid(h-1, v) == True): #down
        node = [h-1, v]
        queue.append(node)
        search(node, queue)
    #If it is not possible, return to last visited node and try another path
    else:
        queue.pop()
        node = queue[len(queue) - 1]
        print("Returning to node: ", node)
        search(node, queue)

#A node is valid whether it exists in maze's dimentions, or is neither a wall or already visited node
def valid(h, v):
    if not(0<=h<hor and 0<=v<ver):
        return False
    elif (maze[h, v]=="#" or maze[h, v]=="o"):
        return False
    else:
        return True

#Defining maze
maze = np.array([["#", "#","#","*","*", "*","#","#"],
                ["#", "*","*","*","#", "*","#","#"],
                ["#", "*","#","#","#", "*","#","#"],
                ["*", "*","*","*","#", "G","#","#"],
                ["*", "#","#","#","#", "*","#","#"],
                ["*", "#","#","*","*", "*","#","#"],
                ["*", "#","#","*","#", "#","#","#"],
                ["S", "*","*","*","#", "#","#","#"]])

#Defining maze's dimentions and queue
hor = 8
ver = 8


#Finding start and goal points
for h in range(0, hor):
    for v in range (0, ver):
        if (maze[h,v] == "G"):
            goal = [h,v]
        elif (maze[h,v] == "S"):
            start = [h,v]

#Main
queue=[start]
print("Original maze:",maze, sep='\n')
search(start, queue)
print("Solved maze:",maze, sep='\n')
print("Path traveled: ", queue)
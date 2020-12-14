import cv2
import numpy as np
import collections

def search(queue):
    if not queue:   #If all possible nodes are visited
        return
    node = queue[0] #Check first element in queue
    h, v = node[:2] #Find current position in maze
    maze[h, v] = "o"  #Mark node as visited

    # Check avalible moves and if valid add to queue:
    if (valid(h, v - 1) == True):  # left
        queue.append([h, v-1])
    if (valid(h, v+1) == True): #right
        queue.append([h, v + 1])
    if (valid(h+1, v) == True): #up
        queue.append([h + 1, v])
    if (valid(h-1, v) == True): #down
        queue.append([h - 1, v])
    #Dequeue current poosition
    queue.popleft()
    #Repeat for the next node
    search(queue)

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

#Defining maze's dimentions
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
queue=collections.deque([start])
print("Original maze:",maze, sep='\n')
search(queue)
print("Solved maze:",maze, sep='\n')
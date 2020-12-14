import cv2
import numpy as np
import collections

#Sort priority queue by lowest F score
def sort(l):
    return l['F_score']

#Calculate G_score - (steps we had to take to get to this node from start)
def G_score(path):
    G = len(path)-1
    return G

#Calculate H score - distance from goal (assumed, by Manhattan distance)
def H_score(node):
    h, v = node[:2]
    H, V = goal[:2]
    Manh_dist = abs(h - H) + abs(v - V)
    return Manh_dist

#Printing solved maze
def print_solved(path):
    for f in range(0, (len(path) - 1)):
        node = path[f]
        h, v = node[:2]
        maze_copy[h, v] = "o"
    print("Solved maze:", maze_copy, sep='\n')

def search(list):
    #Finding the node with lowest F value to perform searching from that node
    list.sort(key=sort)
    #Unpacking from lists, dictionaries etc.
    item = list[0]
    list.pop(0)
    node = item['node']
    path = item['path']
    #Safety and computional purposes - path is mentioned in our big list, we don't want to modify whole list each time we modify variable
    path_copy = path.copy()
    h, v = node[:2]     #we are here in the maze

    #If current node is goal we will print our  stop the algorithm:
    if (node == goal):
        print("A valid path has been found!")
        print_solved(path)
        return

    #For all valid neighbours:
    #we will calculate G and H, add to achieve F and add the value to priority queue ('list')
    if (valid(h, v - 1) == True):  # left
        path_copy.append([h, v-1])
        G = G_score(path)
        H = H_score(node)
        F = G+H
        node = [h, v-1]
        maze[h, v - 1] = "o"        #indicate that node is visited
        list.append({'F_score': F, 'node': node, 'path': path_copy})
        path_copy = path.copy()     #clear all changes we've done to path variable
    if (valid(h, v+1) == True): #right
        path_copy.append([h, v + 1])
        G = G_score(path)
        H = H_score(node)
        F = G + H
        node = [h, v + 1]
        maze[h, v + 1] = "o"
        list.append({'F_score': F, 'node': node, 'path': path_copy})
        path_copy = path.copy()
    if (valid(h+1, v) == True): #up
        path_copy.append([h + 1, v])
        G = G_score(path)
        H = H_score(node)
        F = G + H
        node = [h+1, v]
        maze[h + 1, v] = "o"
        list.append({'F_score': F, 'node': node, 'path': path_copy})
        path_copy = path.copy()
    if (valid(h-1, v) == True): #down
        path_copy.append([h - 1, v])
        G = G_score(path)
        H = H_score(node)
        F = G + H
        node = [h - 1, v]
        maze[h - 1, v] = "o"
        list.append({'F_score': F, 'node': node, 'path': path_copy})
        path_copy = path.copy()

    #Then the function will be called again to expand next node
    search(list)

#A node is valid when it didn't exceed the maze's range or is not a wall or previously visited node
def valid(h, v):
    if not(0<=h<=7 and 0<=v<=13):
        return False
    elif (maze[h, v]=="#" or maze[h, v]=="o"):
        return False
    else:
        return True

#Defining maze
maze = np.array([["#", "#","#","*","*", "*","*","*", "#", "#", "*", "#", "#"],
                ["#", "*","*","*","#", "#","*","#", "#", "#", "*", "#", "#"],
                ["#", "*","#","#","#", "#","*","*", "*", "*", "*", "#", "#"],
                ["*", "*","*","*","#", "#","#","#", "#", "#", "G", "*", "*"],
                ["*", "#","#","#","#", "#","#","#", "#", "#", "#", "#", "*"],
                ["*", "#","#","*","*", "*","#","*", "*", "*", "#", "*", "*"],
                ["*", "#","#","*","#", "*","#","*", "#", "*", "#", "*", "#"],
                ["S", "*","*","*","#", "*","*","*", "#", "*", "*", "*", "#"]])

#Defining start and goal points
start = [7, 0]
goal = [3, 10]

###Main###

#Initialize priority que with start node and display maze to solve
list = [{'F_score': 0, 'node': start, 'path': [start]}]       #element in {} is dictionary, thus 'list' is list of dictionaries, key 'path' contains list of visited nodes
print("Original maze:",maze, sep='\n')

#Safety and computional purposes - changes in the maze are done in search() algorithm, but we need original maze to display final results on
maze_copy = maze.copy()
#Main algorithm
search(list)

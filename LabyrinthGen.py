"""
Labyrinth generator v. 2.0c (roguelike)

Features in 2.0c:
- dig now starts from half the lab size
- labyrinth generation is now timed
- solve under construction

3D version demo:
www.instagram.com/p/BQszVwBhoYT/

Coded by Kuba Siekierzynski (c) 2017
Original code:
https://code.sololearn.com/cL8CKWRqS2XN/#py

My tribute to ADOM (Ancient Domains of Mystery - www.adom.de)

"""

import random
import sys
import time

ADOM = {0: '.', 1: '#', 2: '<', 3: '>', 4: ','}
SIZE = (19, 39)
HSIZE = (SIZE[0] * 2 + 1, SIZE[1] * 2 + 1)
# ADOM - dictionary translating to lab tiles
# SIZE - of the labyrinth (x, y)
# HSIZE - the size of hash_lab

if sys.getrecursionlimit() < SIZE[0] * SIZE[1]:
    sys.setrecursionlimit(SIZE[0] * SIZE[1])
# if max recursion limit is lower than needed, adjust it

N, S, E, W = 1, 2, 4, 8
# directions translated into bitnums to store information on all cleared walls in one variable per cell

GO_DIR = {N: (0, -1), S: (0, 1), E: (1, 0), W: (-1, 0)}
# dictionary with directions translated to digging moves

REVERSE = {E: W, W: E, N: S, S: N}
# when a passage is dug from a cell, the other cell obtains the reverse passage, too

lab = list(list(0 for i in range(SIZE[0])) for j in range(SIZE[1]))
visited = list(lab)
# labyrinth is prepared

def dig(x, y):
    # digs passage from a cell (x, y) in an unvisited cell
    dirs = [N, E, W, S]
    random.shuffle(dirs)
    # shuffles directions each time for more randomness
    for dir in dirs:
        new_x = x + GO_DIR[dir][0]
        new_y = y + GO_DIR[dir][1]
        if (new_y in range(SIZE[1])) and\
        (new_x in range(SIZE[0])) and\
        (lab[new_y][new_x] == 0):
            # checks if the new cell is not visited
            lab[y][x] |= dir
            lab[new_y][new_x] |= REVERSE[dir]
            # if so, apply info on passages to both cells
            dig(new_x, new_y)
            # repeat recursively



def solve(x1, y1, x2, y2):
    # solves a path  from start (x1, y1) to end (x2, y2)
    dirs = [N, E, W, S]

    def min_dir(x, y):
        temp_dir = 100
        vis = 100
        # determines which direction to go
        for dir in dirs:
            dir_x = x + GO_DIR[dir][0]
            dir_y = y + GO_DIR[dir][1]
            if (dir_y in range(SIZE[1])) and (dir_x in range(SIZE[0])) and (lab[y][x] & dir != 0):
                if visited[dir_y][dir_x] <= vis:
                    vis = visited[dir_y][dir_x]
                    temp_dir = dir
        return temp_dir
        
"""    
    # shuffles directions each time for more randomness
    for dir in dirs:
        new_x = x1 + GO_DIR[dir][0]
        new_y = y1 + GO_DIR[dir][1]
        if (new_y in range(SIZE[1])) and\
        (new_x in range(SIZE[0])) and\
        (lab[new_y][new_x] == 0):
            # checks if the new cell is not visited
            lab[y][x] |= dir
            lab[new_y][new_x] |= REVERSE[dir]
            # if so, apply info on passages to both cells
            solve(new_x, new_y)
            # repeat recursively

- preparing the solve() function - some notes below for further decision-making:
- recursion vs while True loop (until (x2, y2) reached on path list)
- visited - number (min number of visits each time)
- path - list of cells' coordinates (append good ones, pop bad ones)
- backtracking status - processing new branch or withdrawing from dead-end - needed True/False to determine if the crossroad cell should be marked as visited more than once (not if back from a dead-end and checking a new alternative - maybe manually putting the minus)
- backward tracking on the branch:
    - if min num of visits = 0 - it's a new path to check - append each visited cell to the path list, decrease by one the number of visits on the crossroad cell, invert backtracking status
    - if min num of visits = 1 - it's a dead-end - pop the whole branch from path list (one by one) until a crossroads with unvisited branches reached; then proceed the new path
    - apply path to hash_lab to display during print (,.:;)

"""
    
def check():
    # displays the cells' values for check-up
    for i in range(SIZE[1]):
        for j in range(SIZE[0]):
            print(" "*(1-(lab[i][j]//10))+\
            str(lab[i][j]), end='|')
        print ('')

    
def draw_hash():
    # generates the labyrinth in a roguealike style :)
    print ("Visit: www.instagram.com/p/BQszVwBhoYT/"+"\n\nADOM-like Labyrinth of Kuba #" + str(seed) + " (" + str(HSIZE[0])+"x"+str(HSIZE[1])+")")
    # prints the seed (for reference) and the lab size    
    hash_lab = list(list(0 for i in range(HSIZE[0])) for j in range(HSIZE[1]))
    
    # create the hash_lab frame
    for i in range(HSIZE[0]):
        hash_lab[0][i] = 1
        hash_lab[HSIZE[1]-1][i] = 1
    for j in range(HSIZE[1]):
        hash_lab[j][0] = 1
        hash_lab[j][HSIZE[0]-1] = 1
    
    # add cross-section walls to hash_lab
    for j in range(0, HSIZE[1], 2):
        for i in range(0, HSIZE[0], 2):
            hash_lab[j][i] = 1
    
    # translate lab to hash_lab
    for j in range(SIZE[1]):
        for i in range(SIZE[0]):
            if (lab[j][i] & S == 0):
                hash_lab[(j+1)*2][(i+1)*2-1] = 1
            if (lab[j][i] & E == 0):
                hash_lab[(j+1)*2-1][(i+1)*2] = 1        
    
    # add up- and down- staircases
    hash_lab[1][1] = 2
    hash_lab[HSIZE[1]-2][HSIZE[0]-2] = 3

    # generate the maze level
    for j in range(0, HSIZE[1]):
        for i in range(0, HSIZE[0]):
            print(ADOM[hash_lab[j][i]], end='')
        print("")
            


# Let's start!
seed = random.randint(0, 1000)
random.seed(seed)
start_time = time.time()
dig(SIZE[0]//2, SIZE[1]//2)
end_time = time.time()
draw_hash()
print('\nLabyrinth generated in {:.2f} ms'.format((end_time - start_time)*1000))

# check()

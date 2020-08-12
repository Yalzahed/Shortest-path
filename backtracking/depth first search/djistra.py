import numpy as np 

grid = np.zeros((5,5))

grid[0][0] =2
grid [4][4] = 1
grid[3][2] = -1
length = {
    
}

target_found= False
unvisited_verteces = []
visited_vertices = []
shortest_path_tree = []
start = None 
target = None 
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i][j] == 1:
            start = (i,j)
        if grid[i][j] == 2:
            target = (i,j)
        unvisited_verteces.append((i,j))

length[start] = [0,None]


while not target_found:
    x = float('inf')
    block = None 
    for node in length:
        if  node not in visited_vertices:
            if length[node][0] < x:
                x = length[node][0]
                block = node 

    if (block[0]+1) >= grid.shape[0]:
        pass
    elif grid[block[0]+1][block[1]]==-1: 
        pass 
    elif (block[0]+1,block[1]) in length:
        if length[(block[0]+1,block[1])][0] > length[block][0]+1:
            length[(block[0]+1,block[1])] = [length[block][0]+1,block]
    else:
        length[(block[0]+1,block[1])] = [length[block][0]+1,block]


    if (block[1]+1) >= grid.shape[1]:
        pass
    elif grid[block[0]][block[1]+1]== -1: 
        pass
    elif  (block[0],block[1]+1) in length:
        if length[(block[0],block[1]+1)][0] > length[block][0]+1:
            length[(block[0],block[1]+1)] = [length[block][0]+1,block]
    else:
        length[(block[0],block[1]+1)] = [length[block][0]+1,block]


    if (block[0]-1) < 0:
        pass
    elif grid[block[0]-1][block[1]]==-1: 
        pass 
    elif (block[0]-1,block[1]) in length:
        if length[(block[0]-1,block[1])][0] > length[block][0]+1:
            length[(block[0]-1,block[1])] = [length[block][0]+1,block]
    else:
        length[(block[0]-1,block[1])] = [length[block][0]+1,block]


    if (block[1]-1) < 0:
        pass
    elif grid[block[0]][block[1]-1]==-1: 
        pass 
    elif (block[0],block[1]-1) in length:
        if length[(block[0],block[1]-1)][0] > length[block][0]+1:
            length[(block[0],block[1]-1)] = [length[block][0]+1,block]
    else:
        length[(block[0],block[1]-1)] = [length[block][0]+1,block]

    visited_vertices.append(block)

    if target in length:
        target_found = True 
print(length)
shortest_path = []
shortest_path.append(target)
while start not in shortest_path:
    x = shortest_path[-1]
    shortest_path.append(length[x][1])

print("\n")
print(shortest_path)
print(grid)
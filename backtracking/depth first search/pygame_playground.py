import pygame, numpy as np
from pygame.locals import *

ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DISPLAY_HEIGHT = 400
DISPLAY_WIDTH = 400

pygame.init()

screen = pygame.display.set_mode((DISPLAY_HEIGHT, DISPLAY_WIDTH))
screen.fill(WHITE)

grid = np.zeros((20,20))
blockSize = 20

def drawgrid():
    blockSize = 20
    for x in range(20):
        for y in range(20):
            rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
            pygame.draw.rect(screen,BLACK,rect,1)

length =  {}

target_found= False
unvisited_verteces = []
visited_vertices = []
shortest_path_tree = []
start = None 
target = None

# def Dijkstra(grid):
#     target_found= False
#     visited_vertices = []
#     length = {}
#     start = None 
#     target = None
#     for i in range(grid.shape[0]):
#         for j in range(grid.shape[1]):
#             if grid[i][j] == 1:
#                 start = (i,j)
#             if grid[i][j] == 2:
#                 target = (i,j)
#     length[start] = [0,None]
   
#     while not target_found:
#         x = float('inf')
#         block = None 
#         for node in length:
#             if  node not in visited_vertices:
#                 if length[node][0] < x:
#                     x = length[node][0]
#                     block = node 

#         if (block[0]+1) >= grid.shape[0]:
#             pass
#         elif grid[block[0]+1][block[1]]==-1: 
#             pass 
#         else:
#             length[(block[0]+1,block[1])] = [length[block][0]+1,block]

#         if (block[1]+1) >= grid.shape[1]:
#             pass
#         elif grid[block[0]][block[1]+1]== -1: 
#             pass 
#         else:
#             length[(block[0],block[1]+1)] = [length[block][0]+1,block]

#         if (block[0]-1) <= grid.shape[0]:
#             pass
#         elif grid[block[0]-1][block[1]]==-1: 
#             pass 
#         else:
#             length[(block[0]-1,block[1])] = [length[block][0]+1,block]

#         if (block[1]-1) <= grid.shape[1]:
#             pass
#         elif grid[block[0]][block[1]-1]==-1: 
#             pass 
#         else:
#             length[(block[0],block[1]-1)] = [length[block][0]+1,block]

#         visited_vertices.append(block)
#         if target in length:
#             target_found = True 

#     shortest_path_tree = []
#     shortest_path_tree.append(target)
#     while start not in shortest_path_tree:
#         x = shortest_path_tree[-1]
#         shortest_path_tree.append(length[x][1])
#     return shortest_path_tree



counter = 0
while True:
    drawgrid()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                x_loc,y_loc = event.pos
                x = x_loc//20
                y = y_loc//20
                if grid[y][x] == 0:
                    grid[y][x] = -1
                    rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                    pygame.draw.rect(screen,BLACK,rect)


                elif grid[y][x] == -1:
                    grid[y][x] = 0
                    rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                    pygame.draw.rect(screen,WHITE,rect)

            elif event.button == 3: 
                x_loc,y_loc = event.pos
                x = x_loc//20
                y = y_loc//20
                if grid[y][x] == 0 and counter < 2 and start == None:
                    grid[y][x] = 1
                    rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                    pygame.draw.rect(screen,ORANGE,rect)
                    start = (y,x)
                    counter +=1

                    print(start)
                elif grid[y][x] == 0 and counter < 2 and start != None:
                    grid[y][x] = 2
                    rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                    pygame.draw.rect(screen,ORANGE,rect)
                    target = (y,x)
                    counter +=1

                    print(target)
                elif grid[y][x] == 1:
                    grid[y][x] = 0
                    rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                    pygame.draw.rect(screen,ORANGE,rect)
                    counter -=1
        elif event.type == KEYDOWN:



            length[start] = [0,None]
            print(target)
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
                        y = block[0]+1
                        x = block[1]
                        rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                        pygame.draw.rect(screen,RED,rect)
                        drawgrid()
                        pygame.display.update()
                        pygame.time.wait(20)


                else:
                    length[(block[0]+1,block[1])] = [length[block][0]+1,block]
                    y = block[0]+1
                    x = block[1]
                    rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                    pygame.draw.rect(screen,RED,rect)
                    drawgrid()
                    pygame.display.update()
                    pygame.time.wait(20)
                        
                if (block[1]+1) >= grid.shape[1]:
                    pass
                elif grid[block[0]][block[1]+1]== -1: 
                    pass
                elif  (block[0],block[1]+1) in length:
                    if length[(block[0],block[1]+1)][0] > length[block][0]+1:
                        length[(block[0],block[1]+1)] = [length[block][0]+1,block]
                        y = block[0]
                        x = block[1]+1
                        rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                        pygame.draw.rect(screen,RED,rect)
                        drawgrid()
                        pygame.display.update()
                        pygame.time.wait(20)

                else:
                    length[(block[0],block[1]+1)] = [length[block][0]+1,block]
                    y = block[0]
                    x = block[1]+1
                    rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                    pygame.draw.rect(screen,RED,rect)
                    drawgrid()
                    pygame.display.update()
                    pygame.time.wait(20)

                if (block[0]-1) < 0:
                        pass
                elif grid[block[0]-1][block[1]]==-1: 
                    pass 
                elif (block[0]-1,block[1]) in length:
                    if length[(block[0]-1,block[1])][0] > length[block][0]+1:
                        length[(block[0]-1,block[1])] = [length[block][0]+1,block]
                        y = block[0]-1
                        x = block[1]
                        rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                        pygame.draw.rect(screen,RED,rect)
                        drawgrid()
                        pygame.display.update()
                        pygame.time.wait(20)

                else:
                    length[(block[0]-1,block[1])] = [length[block][0]+1,block]
                    y = block[0]-1
                    x = block[1]
                    rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                    pygame.draw.rect(screen,RED,rect)
                    drawgrid()
                    pygame.display.update()
                    pygame.time.wait(20)

                if (block[1]-1) < 0:
                        pass
                elif grid[block[0]][block[1]-1]==-1: 
                    pass 
                elif (block[0],block[1]-1) in length:
                    if length[(block[0],block[1]-1)][0] > length[block][0]+1:
                        length[(block[0],block[1]-1)] = [length[block][0]+1,block]
                        y = block[0]
                        x = block[1]-1
                        rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                        pygame.draw.rect(screen,RED,rect)
                        drawgrid()
                        pygame.display.update()
                        pygame.time.wait(20)
                else:
                    length[(block[0],block[1]-1)] = [length[block][0]+1,block]
                    y = block[0]
                    x = block[1]-1
                    rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                    pygame.draw.rect(screen,RED,rect)
                    drawgrid()
                    pygame.display.update()
                    pygame.time.wait(20)
                visited_vertices.append(block)
                if target in length:
                    target_found = True 

            shortest_path = []
            shortest_path.append(target)

            while start not in shortest_path:
                x = shortest_path[-1]
                shortest_path.append(length[x][1])
            for step in shortest_path:
                y = step[0] 
                x = step[1]
                rect = pygame.Rect(x*blockSize,y*blockSize,blockSize,blockSize)
                pygame.draw.rect(screen,GREEN,rect)
                drawgrid()
                pygame.display.update()
                pygame.time.wait(100)

    pygame.display.update()















# size = 640, 320
# width, height = size 
# GREEN = (150,255,150)
# RED = (255,0,0)



# pygame.init()

# screen = pygame.display.set_mode(size)
# running = True

# ball = pygame.image.load("C:/Users/yasse/Desktop/learning projects/backtracking/depth first search/ball.gif")
# rect = ball.get_rect()
# speed = [2,2]

# while running:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False


#     rect = rect.move(speed)
#     if rect.left < 0 or rect.right > width: 
#         speed[0] = -speed[0]
#     if rect.top < 0 or rect.bottom > height:
#         speed[1] = -speed[1]
#     screen.fill(GREEN)
#     pygame.draw.circle(screen,RED,(10,50),1)
#     screen.blit(ball,rect)
#     pygame.display.update()
#     pygame.time.wait(10)

# pygame.quit()




#-------------------------------------------------------------------------------------------









# screen = pygame.display.set_mode((640,240))

# BLACK = (0,0,0)
# GRAY = (127,127,127)
# WHITE = (255,255,255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# CYAN = (0, 255, 255)
# MAGENTA = (255, 0, 255)
# background = GRAY
# running = True 
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_r:
#                 background = RED
#             if event.key == pygame.K_g:
#                 background = GREEN
#     screen.fill(background)
#     pygame.display.update()
# pygame.quit()
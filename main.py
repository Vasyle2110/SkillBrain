import os
import time

def snakeHeads(startX,startY,ct,snake,m):
    if ct == 0:
        m[startX][startY] = snake[0]
    else:
        startX = startX + 1
        m[startX][startY] = snake[0]

def spaceGenerator(rows,col,ct,snake,m,startX,startY):
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(1, rows - 1):
        for j in range(1, col - 1):
            m[i][j] = ' '

    for i in range(0,rows):
        m[i][0] = 'X'
        m[i][col-1] = 'X'
    for i in range(0,col):
        m[0][i] = 'X'
        m[rows-1][i] = 'X'
    if ct == 0:
        m[startX][startY] = snake[0]
    else:
        m[startX][startY] = snake[0]
    for x in m:
        print(*x)


x = int(input("Enter number of lines: "))
y = int(input("Enter number of columns: "))
m = [[' ' for _ in range(y)]for _ in range(x)]
startX = x // 2
startY = y // 2

ct = 0
snake = ['#']
while(True):
    spaceGenerator(x,y,ct,snake,m,startX,startY)
    startY = startY + 1
    ct += 1
    time.sleep(1)

import random, time, os, keyboard
from termcolor import colored
clear = lambda: os.system('clear')

ROW = 51
COL = 51
# Gold pos number of gold and its (X, Y) Position
goldPos = []
for i in range(random.randint(5,20)):
    temp = []
    temp.append(random.randint(1,ROW-1))
    temp.append(random.randint(1,COL-2))
    goldPos.append(temp)

sharkPos = []
for i in range(random.randint(1,8)):
    temp = []
    temp.append(random.randint(1,ROW-1))
    temp.append(random.randint(1,COL-2))
    sharkPos.append(temp)

prevChoice = 0


class Grid():

    def create(self, arr):
        for i in range(COL):
            l = []
            for x in range(ROW):
                if x == ROW - 1 or x == 0:
                    l.append(colored('.', 'white', 'on_green'))
                elif i == 0 or i == COL - 1:
                    l.append(colored('.', 'white', 'on_green'))
                else:
                    l.append(' ')
            arr.append(l)

    def update(self, arr, x, y):
        self.create(arr)
        global prevChoice
        clear()
        for gold in range(len(goldPos)):
            arr[goldPos[gold][1]][goldPos[gold][0]] = colored('G', 'white', 'on_yellow')
        # Shark movement
        for pos in range(len(sharkPos)):

            choice = random.randint(0, 4)
            prevChoice = choice
            if choice == 0:
                if 1 < sharkPos[pos][0]: sharkPos[pos][0] -= 1
            if choice == 1:
                if len(arr[0]) - 2 > sharkPos[pos][0]: sharkPos[pos][0] += 1
            if choice == 2:
                if 1 < sharkPos[pos][1]: sharkPos[pos][1] -= 1
            if choice == 3:
                if len(arr[0]) - 2 > sharkPos[pos][1]: sharkPos[pos][1] += 1

            arr[sharkPos[pos][1]][sharkPos[pos][0]] = colored('S', 'white', 'on_blue');

        arr[y][x] = colored('*', 'white', 'on_red')
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


arr = []


def main():
    goldPoints = 0

    grid = Grid()
    grid.create(arr)

    X = int(len(arr[0]) // 2)
    Y = int(len(arr[1]) // 2)

    while True:
        while True:
            try:
                if keyboard.is_pressed('w'):
                    if 1 < Y: Y -= 1
                elif keyboard.is_pressed('a'):
                    if 1 < X: X -= 1
                elif keyboard.is_pressed('s'):
                    if len(arr[1]) - 2 > Y: Y += 1
                elif keyboard.is_pressed('d'):
                    if len(arr[0]) - 2 > X: X += 1

                for i in range(len(goldPos)):
                    if X == int(goldPos[i][0]) and Y == int(goldPos[i][1]):
                        goldPos.pop(i)
                        goldPoints += 1

                for i in range(len(sharkPos)):
                    if X == int(sharkPos[i][0]) and Y == int(sharkPos[i][1]):
                        clear()
                        print('\n\n\t\t\tGAME OVER')
                        os.system('export BEEP=/usr/share/sounds/KDE-Sys-App-Error-Critical.ogg && paplay $BEEP')
                        time.sleep(10); exit()

                if len(goldPos) == 0:
                    clear()
                    print('\n\n\t\t\tYOU WIN')
                    os.system('export BEEP=/usr/share/sounds/Oxygen-Sys-Warning.ogg && paplay $BEEP')
                    time.sleep(10); exit()
                break
            except:
                pass

        time.sleep(0.03)
        arrGrid = []
        grid.update(arrGrid, X, Y)
        print("Gold Points: {}".format(goldPoints))
        print("Gold Left: {}".format(len(goldPos)))
        print('X: {} Y: {}'.format(X, Y))

main()
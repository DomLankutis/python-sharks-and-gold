import random, time, os, keyboard
clear = lambda: os.system('clear')

ROW = 51
COL = 51
# Gold pos number of gold and its (X, Y) Position
goldPos = [[10, 10], [3, 7], [14, 28]]
sharkPos = [[17,1], [43, 30]]

prevChoice = 0
'''
Create a 2D plain and make a character move in such plane
'''
class Grid():

    def create(self, arr):
        for i in range(COL):
            l = []
            for x in range(ROW):
                if x == ROW - 1 or x == 0:
                    l.append(str('.'))
                elif i == 0 or i == COL - 1:
                    l.append('.')
                else:
                    l.append(' ')
            arr.append(l)

    def update(self, arr, x, y):
        self.create(arr)
        global prevChoice
        clear()
        for gold in range(len(goldPos)):
            arr[goldPos[gold][1]][goldPos[gold][0]] = 'G'
        for pos in range(len(sharkPos)):

            choice = random.randint(0, 4)

            if choice == prevChoice:
                choice = random.randint(0, 4)
                prevChoice = choice
            else:
                prevChoice = choice
            if choice == 0:
                if 1 < sharkPos[pos][0]: sharkPos[pos][0] -= 1
            if choice == 1:
                if len(arr[0]) - 2 > sharkPos[pos][0]: sharkPos[pos][0] += 1
            if choice == 2:
                if 1 < sharkPos[pos][1]: sharkPos[pos][1] -= 1
            if choice == 3:
                if len(arr[0]) - 2 > sharkPos[pos][1]: sharkPos[pos][1] += 1

            arr[sharkPos[pos][1]][sharkPos[pos][0]] = 'S'

        arr[y][x] = '*'
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
                        print('True')

                for i in range(len(sharkPos)):
                    if X == int(sharkPos[i][0]) and Y == int(sharkPos[i][1]):
                        clear()
                        print('\n\n\t\t\tGAME OVER')
                        time.sleep(10); exit()
                break
            except:
                pass


        time.sleep(0.03)
        arrGrid = []
        grid.update(arrGrid, X, Y)
        print("Gold Points: {}".format(goldPoints))
        print('X: {} Y: {}'.format(X, Y))
        print('Shark Pos: {}'.format(sharkPos))

main()
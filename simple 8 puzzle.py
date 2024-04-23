import os
from array import *
import copy
from pynput import keyboard
from pynput.keyboard import Key
puzzleFace = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 0])
arr1 = []


def printPuzzleMatrix(array1):
    (print("%s | %s | %s" % (array1[0], array1[1], array1[2],), end="", flush=True),
     print("       %s | %s | %s" % (winningFace[0], winningFace[1], winningFace[2])))
    print("----------")
    print("%s | %s | %s" % (array1[3], array1[4], array1[5]), end="", flush=True),
    print("       %s | %s | %s" % (winningFace[3], winningFace[4], winningFace[5]))
    print("----------")
    print("%s | %s | %s" % (array1[6], array1[7], array1[8]), end="", flush=True),
    print("       %s | %s | %s" % (winningFace[6], winningFace[7], winningFace[8]))
    print("--------------------------")
    os.system('cls>nul')


def move_up():
    for i in puzzleFace:
        if puzzleFace[i] == 0:
            emptyNode = i
    if emptyNode - 3 >= 0:
        x = puzzleFace[emptyNode - 3]
        puzzleFace[emptyNode - 3] = puzzleFace[emptyNode]
        puzzleFace[emptyNode] = x
    else:
        print("invalid move")


def move_down():
    for i in puzzleFace:
        if puzzleFace[i] == 0:
            emptyNode = i
    if emptyNode + 3 < 9:
        x = puzzleFace[emptyNode + 3]
        puzzleFace[emptyNode + 3] = puzzleFace[emptyNode]
        puzzleFace[emptyNode] = x
    else:
        print("invalid move")


def move_right():
    for i in puzzleFace:
        if puzzleFace[i] == 0:
            emptyNode = i
    if emptyNode + 1 != 0 and emptyNode + 1 != 3 and emptyNode + 1 != 6 and emptyNode + 1 != 9:
        x = puzzleFace[emptyNode + 1]
        puzzleFace[emptyNode + 1] = puzzleFace[emptyNode]
        puzzleFace[emptyNode] = x
    else:
        print("invalid move")


def move_left():
    for i in puzzleFace:
        if puzzleFace[i] == 0:
            emptyNode = i
    if emptyNode - 1 != 2 and emptyNode - 1 != 5 and emptyNode - 1 != 8 and emptyNode - 1 != -1:
        x = puzzleFace[emptyNode - 1]
        puzzleFace[emptyNode - 1] = puzzleFace[emptyNode]
        puzzleFace[emptyNode] = x
    else:
        print("invalid move")


def set_winningFace(arr=array('I', [])):
    global winningFace
    winningFace = copy.deepcopy(arr)


def check_win():
    if puzzleFace == winningFace:
        print("Mission accomplished")
        exit()


def arrow_keys(key):
    if key == Key.right:
        move_right()
        printPuzzleMatrix(puzzleFace)
        check_win()
    elif key == Key.left:
        move_left()
        printPuzzleMatrix(puzzleFace)
        check_win()
    elif key == Key.up:
        move_up()
        printPuzzleMatrix(puzzleFace)
        check_win()
    elif key == Key.down:
        move_down()
        printPuzzleMatrix(puzzleFace)
        check_win()
    elif key == Key.esc:
        exit()


set_winningFace(array('i', [1, 2, 3, 4, 5, 6, 7, 8, 0]))


print("enter 9 integers containing a 0 and make sure the numbers are between 1-8 ")
for i in range(0, len(winningFace)):
    arr1.append(int(input()))
    print(arr1)
while 0 not in arr1:
    print("you must enter 0")
    arr1.clear()
    for i in range(0, len(winningFace)):
        arr1.append(int(input()))
        print(type(arr1))

else:
    winningFace = copy.deepcopy(arr1)

    puzzleFace = puzzleFace.tolist()
    if puzzleFace == winningFace:
        print("true")
    printPuzzleMatrix(puzzleFace)

    print("Welcome to 8-puzzle the matrix on the left is yours to control, via the arrow keys move the zero num")

    with keyboard.Listener(on_press=arrow_keys) as listener:
        listener.join()

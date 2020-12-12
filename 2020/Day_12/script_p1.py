import os
import math
import operator


def turn(action,course):
    mag = int(action[1:])
    if action[0] == "L": course += mag
    elif action[0] == "R": course -= mag
    return course

def move(action, course):
    p = [0,0]
    mag = int(action[1:])
    if action[0] == "F":
        p[0] = int(round(mag*math.cos(math.radians(course)),0))
        p[1] = int(round(mag*math.sin(math.radians(course)),0))
    elif action[0] == "N": p[1] = mag
    elif action[0] == "S": p[1] = -mag
    elif action[0] == "E": p[0] = mag
    elif action[0] == "W": p[0] = -mag
    return p


def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_12/"
    os.chdir(path)

    data = list(map(str, open('input.txt').read().splitlines()))

    course = 0
    p = [0,0]

    for action in data:
        if action[0] == "R" or action[0] == "L": course = turn(action, course)
        else: p=[p[i]+move(action,course)[i] for i in range(len(p))]
        print(action, p)
    print(abs(p[0])+abs(p[1]))


if __name__ == "__main__":
    main()

import os
import math
import operator

def move(p,action):
    mag = int(action[1:])
    if action[0] == "F":
        p[0] += p[2]*mag
        p[1] += p[3]*mag
    elif action[0] == "N": p[3] += mag
    elif action[0] == "S": p[3] += -mag
    elif action[0] == "E": p[2] += mag
    elif action[0] == "W": p[2] += -mag
    elif action[0] == "R":
        hyp = math.sqrt(p[3]*p[3]+p[2]*p[2])
        ang_rad = math.atan2(p[3],p[2])-math.radians(mag)
        p[2] = int(round(hyp*math.cos(ang_rad),0))
        p[3] = int(round(hyp*math.sin(ang_rad),0))
    elif action[0] == "L":
        hyp = math.sqrt(p[3]*p[3]+p[2]*p[2])
        ang_rad = math.atan2(p[3],p[2])+math.radians(mag)
        p[2] = int(round(hyp*math.cos(ang_rad),0))
        p[3] = int(round(hyp*math.sin(ang_rad),0))
    return p

def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_12/"
    os.chdir(path)

    data = list(map(str, open('input.txt').read().splitlines()))

    course = 0
    p = [0,0,10,1]

    for action in data:
        p = move(p, action)
        print(action, p)
        
    print(abs(p[0])+abs(p[1]))


if __name__ == "__main__":
    main()

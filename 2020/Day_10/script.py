import os
from itertools import combinations

def part1(data):
    diffs = [0,0,0]
    for x in data:
        if x!= 0:
            diffs[x-outlet-1] += 1
        outlet = x
    print("Part 1:",diffs,diffs[0]*diffs[2])

def check_valid(data):
    if len(data) == 1:
        return 1
    else:
        for x in range(1, len(data)):
            if data[x]-data[x-1] > 3:
                return False
        return True

#main program
def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_10/"
    os.chdir(path)

    data = list(map(int, open('input.txt').read().splitlines()))
    data.sort()
    data.append(max(data)+3)
    data = [0]+data
    part1(data)
    print(data)
    ans = {}
    ans[0] = 1
    for x in data[1:]:
        ans[x] = ans.get(x-3,0) + ans.get(x-2,0) + ans.get(x-1,0)

if __name__ == "__main__":
    main()

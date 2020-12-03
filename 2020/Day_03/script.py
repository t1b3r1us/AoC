import os
path = "/Users/thomasmkirk/Python_Apps/2020_Advent/Day_03/"
os.chdir(path)

data = map(str, open('input.txt').read().splitlines())

treecount = [0,0,0,0,0]
right_slopes = [1,3,5,7,1]
down_slopes = [1,1,1,1,2]
print down_slopes[4]
product = 1
for x in range(0,5,1):
    x_pos = 0
    for y in data[::down_slopes[x]]:
        if x_pos> 30:
            x_pos-=31
        if y[x_pos] == "#":
            treecount[x] +=1
        x_pos += right_slopes[x]

    product *= treecount[x]

print product, treecount

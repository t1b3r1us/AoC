import os

a_file = open("/Users/thomasmkirk/Python_Apps/2020_Advent/Day_01/input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()
a_file.close()

values = [int(i) for i in contents_split]

for x in values: #test
    for y in values:
        if x != y:
            t = x + y
            if t == 2020:
                z = x*y
                print x, y, z
                break

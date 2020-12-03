import os
a = os.getcwd()
print a
a_file = open("/Users/thomasmkirk/Python_Apps/2020_Advent/Day_01/input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

a_file.close()

values = [int(i) for i in contents_split]

for x in values:
    for y in values:
        for z in values:
            if x!=y and x!=z and y!=z:
                sum = x + y + z
                if sum == 2020:
                    print sum
                    print x, y, z
                    print x*y*z
                    break


filepath = '/Users/thomasmkirk/Python_Apps/2020_Advent/Day_02/input.txt'

f = open(filepath,"r")

lines = f.readlines()
f.close()

valid_count = 0
for x_line in range(0,len(lines)):
    string_l = lines[x_line]
    dash_pos = string_l.find("-")
    space_pos = string_l.find(" ")
    length = len(string_l)
    min = int(string_l[0:dash_pos])
    max = int(string_l[dash_pos+1:space_pos])
    character = string_l[space_pos+1]
    pw = string_l[space_pos+4:length-1]
    #print min, max, character, pw
    count = 0
    for x in pw:
        if x == character:
            count += 1
    if count <= max and count >= min:
        valid_count += 1
        print "valid", character, min, max, pw, count, valid_count
    else :
        print "invalid", character, min, max, pw, count, valid_count

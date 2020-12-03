
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
    char = string_l[space_pos+1]
    pw = string_l[space_pos+4:length-1]
    pos_1 = string_l[space_pos+3+min]
    pos_2 = string_l[space_pos+3+max]
    #print min, max, character, pw

    if (pos_1==char and pos_2!=char) or (pos_1!=char and pos_2==char):
        valid_count += 1
        print "valid", pw, char, min, max, valid_count, x_line
    else:
        print "invalid", pw, char, min, max, valid_count, x_line

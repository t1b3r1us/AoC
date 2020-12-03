
filepath = '/Users/thomasmkirk/Python_Apps/2020_Advent/Day_02/input.txt'
with open(filepath) as fp:
        valid_count = 0
        line = fp.readline()
        while line:
            line = fp.readline()
            dash_pos = line.find("-")
            space_pos = line.find(" ")
            length = len(line)
            min = int(line[0:dash_pos])
            max = int(line[dash_pos+1:space_pos])
            character = line[space_pos+1]
            pw = line[space_pos+4:length-1]
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

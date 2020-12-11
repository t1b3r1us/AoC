import os

def count_occ_in_view(data,x,y):
    if data[x][y]== ".": return 0
    occupied = 0
    dir = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
    for z in dir:
        i = x
        j = y
        while (0 <= i < len(data)) and (0 <= j < len(data[1])):
            i += z[0]
            j += z[1]
            if not(0 <= i < len(data)) or not(0 <= j < len(data[1])):
                break
            elif data[i][j] == "#":
                occupied +=1
                break
            elif data[i][j] == "L": break
    return occupied

def count_occ(data):
    count = 0
    for x in range(0,len(data),1):
        for y in range(0,len(data[1]),1):
            if data[x][y] == "#": count +=1
    return count

#main program
def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_11/"
    os.chdir(path)

    data = list(map(str, open('input.txt').read().splitlines()))

    for z in range(0,100):
        temp_data = ['']*len(data)
        for x in range(0,len(data)):
            for y in range(0,len(data[1])):
                seat = data[x][y]
                if seat == '.':
                    new_seat = '.'
                elif seat == 'L':
                    result = count_occ_in_view(data,x,y)
                    if result == 0:
                        new_seat = '#'
                    else:
                        new_seat= 'L'
                elif seat == '#':
                    result = count_occ_in_view(data,x,y)
                    if result >= 5:
                        new_seat = 'L'
                    else:
                        new_seat = '#'
                temp_data[x] = temp_data[x] + new_seat
        if data == temp_data:
            print(z, count_occ(data))
            break
        else:
            data = temp_data

if __name__ == "__main__":
    main()

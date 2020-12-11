import os

def count_occ_adj(data,x,y):
    empty_count = 0
    occupied_count = 0
    for i in range(x-1,x+2,1):
        for j in range(y-1,y+2,1):
            if not(i == x and j ==y ) and (0 <= i < len(data)) and (0<=j< len(data[1])):
                if data[i][j] == "L" or data[i][j] == ".":
                    empty_count += 1
                elif data[i][j] == "#":
                    occupied_count+=1
    return occupied_count

def count_occ(data):
    count = 0
    for x in range(0,len(data),1):
        for y in range(0,len(data[1]),1):
            if data[x][y] == "#":
                count +=1
    return count

#main program
def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_11/"
    os.chdir(path)

    data = list(map(str, open('input.txt').read().splitlines()))
    print(len(data[1]), len(data))

    for z in range(0,10000):
        temp_data = ['']*len(data)
        for x in range(0,len(data)):
            for y in range(0,len(data[1])):
                seat = data[x][y]
                if seat == '.':
                    new_seat = '.'
                elif seat == 'L':
                    result = count_occ_adj(data,x,y)
                    if result == 0:
                        new_seat = '#'
                    else:
                        new_seat= 'L'
                elif seat == '#':
                    result = count_occ_adj(data,x,y)
                    if result >= 4:
                        new_seat = 'L'
                    else:
                        new_seat = '#'
                temp_data[x] = temp_data[x] + new_seat
        if data == temp_data:
            print(z, count_occ(data))
            break
        else:
            data = temp_data

    print(len(data[1]), len(data))

if __name__ == "__main__":
    main()

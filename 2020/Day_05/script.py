import os

def seat_id(bp):
    row = 0
    column = 0

    range_size = 128
    for x in range(0,7):
        range_size /= 2
        if bp[x]=="B":
            row = row + range_size

    range_size = 8
    for x  in range(7,10):
        range_size /= 2
        if bp[x]=="R":
            column = column + range_size
    return row*8+column

def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_05/"
    os.chdir(path)
    data = map(str, open('input.txt').read().splitlines())
    seat_ids = [0]*len(data)
    cnt=0
    max_seat_id = 0
    for bp in data:
        seat_ids[cnt] = seat_id(bp)
        cnt+=1
        if seat_id(bp)>max_seat_id:
            max_seat_id = seat_id(bp)

    print "Part 1. The max seat ID is", max_seat_id
    #Part 2
    seat_ids.sort()
    for x in range(0,len(seat_ids)-1):
        if (seat_ids[x+1]-seat_ids[x])==2:
            print "Part 2: My seat ID is", seat_ids[x]+1

if __name__ == "__main__":
    main()

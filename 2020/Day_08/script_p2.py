import os


#main program
def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_08/"
    os.chdir(path)
    data = list(map(str, open('input.txt').read().splitlines()))

    run = [0]*len(data)
    switch = [0]*len(data)
    switch_temp = 0
    x = 0
    acc = 0
    end_of_data = False

    while end_of_data == False:
        if x==len(data):
            print("Reached end of data acc = ", acc, "line switched = ", switch_temp, data[switch_temp])
            end_of_data = True
            break
        elif run[x] == 1:
            x = 0
            acc = 0
            run = [0]*len(data)
            switch_temp = 0
        else:
            run[x] += 1
            if data[x][0:3] == "nop":
                if switch[x] == 1 or x == 0 or switch_temp > 0:
                    x += 1
                else:
                    switch[x] = 1
                    switch_temp = x
                    x += int(data[x][3:])
            elif data[x][0:3] == "acc":
                acc += int(data[x][3:])
                x += 1
            else:

                if switch[x] == 1 or switch_temp > 0:
                    x += int(data[x][3:])
                else:
                    switch[x] = 1
                    switch_temp = x
                    x += 1

if __name__ == "__main__":
    main()

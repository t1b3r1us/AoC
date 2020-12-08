import os

#main program
def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_08/"
    os.chdir(path)

    data = list(map(str, open('input.txt').read().splitlines()))
    run = [0]*len(data)
    x = 0
    acc = 0
    while run.count(2) == 0:
        if run[x] == 1:
            break
        else:
            run[x] += 1
            if data[x][0:3] == "nop":
                x += 1
            elif data[x][0:3] == "acc":
                acc += int(data[x][3:])
                x += 1
            else:
                x += int(data[x][3:])

    print("First repeating value:", data[x],"index = ", x,  "acc =", acc, ", number of runs =", sum(run))

if __name__ == "__main__":
    main()

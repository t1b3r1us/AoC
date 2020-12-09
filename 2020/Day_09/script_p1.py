import os

def find_num(data, preamble_l):
    for x in range(preamble_l, len(data)):
        combo_found = 0
        for y in data[x-preamble_l:x]:
            for z in data[x-preamble_l:x]:
                if y == z:
                    break
                elif (y+z)==data[x]:
                    combo_found = 1
                    break
        if combo_found == 0:
            return [data[x], x]

def add_values(data,nums_to_add,index,value): #increasing
    if nums_to_add == 0:
        return value
    else:
        value += data[index]
        nums_to_add -= 1
        index += 1
        return add_values(data, nums_to_add, index, value)

#main program
def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_09/"
    os.chdir(path)

    data = list(map(int, open('input.txt').read().splitlines()))

    preamble_l = 25
    val = find_num(data, preamble_l)
    print("Val = ", val[0])
    set_found = False
    num_to_add = 1
    while(set_found == False):
        num_to_add += 1
        for x in range(1,len(data)-num_to_add+1):
            #print(add_values(data,num_to_add,x,0))
            if add_values(data,num_to_add,x,0) == val[0]:
                set_found = True
                break

    print("\n\nContiguous numbers =")
    for y in data[x:x+num_to_add]:
        print(y)
    print("\nMax + min =", max(data[x:x+num_to_add])+min(data[x:x+num_to_add]))

if __name__ == "__main__":
    main()

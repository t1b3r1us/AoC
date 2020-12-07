import os
import re
import sys
global_sum = 0
#find bag on list and return subbags
def find_subbags(bag, data, sum, num_bags):
    global global_sum
    print("\nsub_bag input =", bag)

    for y in range(0,len(data)):
        if re.search("(.*?)\sbag", data[y]).group(1) == bag:
            break
    print(y, data[y])

    if data[y].count(" contain no other bags."):
        print("end detected")
        return 0
    else :
        sub_bags = re.findall("[1-9]\s(.*?)\sbag", data[y])
        print("sub_bags found", sub_bags)
        for x in sub_bags:
            num_bags_temp = int(re.search(r"(\d+) %s" % x, data[y]).group(1))
            print(x, "     ", num_bags_temp)
            sum += num_bags_temp*num_bags
            global_sum += num_bags_temp*num_bags
            print(num_bags_temp, num_bags, sum)
            find_subbags(x, data, sum, num_bags_temp*num_bags)


#main program
def main():
    global gold
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_07/"
    os.chdir(path)

    data = list(map(str, open('input.txt').read().splitlines()))

    bag = "shiny gold"
    bags = find_subbags(bag, data, 1, 1)
    print(global_sum)

if __name__ == "__main__":
    main()

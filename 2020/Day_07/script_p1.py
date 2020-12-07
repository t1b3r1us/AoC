import os
import re
import sys

gold = 0

#find first bag on line
def first_bag(index, data):
    return re.search("(.*?)\sbag", data[index]).group(1) #First bag on line

#find bag on list and return subbags
def find_subbags(bag, data):
    global gold
    print("\nsub_bag input =", bag)

    for y in range(0,len(data)):
        if re.search("(.*?)\sbag", data[y]).group(1) == bag:
            break

    if bag == 'shiny gold':
        #print("Sub bags found shiny gold")
        gold = 1
    elif data[y].count(" contain no other bags."):
        print("No bags")
    else : #re.search("(.*?)\sbag", y).group(1) == bag:
        sub_bags = re.findall("[1-9]\s(.*?)\sbag", data[y])
        print("sub_bags found", sub_bags)
        for x in sub_bags:
            find_subbags(x,data)

#main program
def main():
    global gold
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_07/"
    os.chdir(path)

    data = list(map(str, open('input.txt').read().splitlines()))

    shiny_gold_count=0
    for index in range(0,len(data)):
        gold = 0
        bag = first_bag(index,data)
        if bag != 'shiny gold':
            find_subbags(bag, data)
            if gold == 1:
                shiny_gold_count += 1

    print("Shiny gold count =", shiny_gold_count)

if __name__ == "__main__":
    main()

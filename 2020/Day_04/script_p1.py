import os
path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_04/"
os.chdir(path)
#comment

def part1(data):
    result = [-1]*8
    fields = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:","cid:"]
    for x in range(0,len(fields)):
        result[x] = data.find(fields[x])
    thing_index = result[0:7].index(-1) if -1 in result[0:7] else -1
    print result, thing_index
    if thing_index == -1:
        print "valid"
        return 1
    else :
        print "invalid"
        return -1

def main():
    valid_count = 0
    invalid_count = 0
    cnt = 0
    line_cnt =0

    lines = open("input.txt","r").read().splitlines()

    string = ''
    for line in lines:
        string = string + " " + line
        line_cnt +=1
        if line =='' or line_cnt == len(lines):
            cnt += 1
            if part1(string) == 1:
                valid_count += 1
                print "valid", valid_count, string
            else:
                invalid_count += 1
                print "invalid", invalid_count, string
            string = ''

    print line_cnt, "total = ", cnt, "Valid count = ", valid_count, "invalid_count = ", invalid_count
    return 0

if __name__ == '__main__':
  main()

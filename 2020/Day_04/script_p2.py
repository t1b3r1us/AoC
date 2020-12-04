import os
import re
path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_04/"
os.chdir(path)

def part1(data):
    result = [-1]*8
    fields = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:","cid:"]
    for x in range(0,len(fields)):
        result[x] = data.find(fields[x])
    thing_index = result[0:7].index(-1) if -1 in result[0:7] else -1
    #print result, thing_index
    if thing_index == -1:
        #print "valid"
        return part2(data)
    else :
        #print "invalid"
        return 0

def part2(data):
    fields = ["byr\:","iyr\:","eyr\:","hgt\:","hcl\:","ecl\:","pid\:"]
    invalid = 0
    for field in fields:
        result = re.search("%s(.*?)\s" % field, data).group(1)
        #print field, result
        if field == fields[0]:
            if int(result)<1920 or int(result)>2002:
                invalid = 1
        elif field == fields[1]:
            if int(result)<2010 or int(result)>2020:
                invalid = 1
        elif field == fields[2]:
            if int(result)<2020 or int(result)>2030:
                invalid = 1
        elif field == fields[3]:
            if result[-2:] != "cm" and result[-2:] != "in":
                invalid = 1
            elif result[-2:] == "cm":
                if not(int(result[:-2])>=150 and int(result[:-2])<=193):
                    invalid = 1
            elif (result[-2:] == "in"):
                if not(int(result[:-2])>=59 and int(result[:-2])<=76):
                    invalid = 1
        elif field == fields[4]:
            if result[0] != "#" or len(result) != 7 or (re.search('[^abcdef0123456789]', result[1:])!=None):
                invalid = 1
        elif field == fields[5]:
            if result not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                invalid = 1
        elif field == fields[6]:
            if (len(result)!=9) or re.search('[^0123456789]', result)!=None:
                invalid = 1
    if invalid ==1:
        return 0
    else:
        return 1

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
            string = string + " "
            cnt += 1
            if part1(string) == 1:
                valid_count += 1
            else:
                invalid_count += 1
            string = ''
    print "valid = ", valid_count
    print "invalid = ", invalid_count
    return 0

if __name__ == '__main__':
  main()

import os


def main():
    path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_06/"
    os.chdir(path)

    lines = open('input.txt').read().splitlines()

    answers = [0]*26
    answers_temp = [0]*26
    total = 0
    line_cnt=0
    pas_cnt = 0
    for line in lines:
        print line
        line_cnt +=1

        if line =='':
            total += sum(answers)
            print pas_cnt, answers, sum(answers), total
            print "\nNew Passenger"
            answers = [0]*26
            pas_cnt = 0
        else:
            pas_cnt +=1
            if pas_cnt == 1:
                for x in line:
                    answers[ord(x)-97]=1
            else:
                for x in line:
                    answers_temp[ord(x)-97]=1
                answers=[answers[i]*answers_temp[i] for i in range(len(answers))]
                #print answers
                answers_temp = [0]*26

    total += sum(answers)
    print pas_cnt, answers, sum(answers), total

if __name__ == "__main__":
    main()

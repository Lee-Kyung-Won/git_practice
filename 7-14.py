in_file = open('vacabulary.txt', 'r')

for line in in_file:
    line = line.strip().split(" ")

    answer = input("%s " % line[0])

    if answer == line[1]:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % line[0])

in_flie.close
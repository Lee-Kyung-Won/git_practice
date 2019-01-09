in_file = open('chicekn.txt', 'r')

day = 0

for line in in_file:
    data = line.strip().split(": ")
    day += 1

    for i in range(day):
        amount += int(data[i])

average = amount // day

in_file.close()

print("경원")
from randam import randint

ANSWER = randint(0, 9)
tries = 4
while tries > 0:
    num = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % tries))
    if ANSWER > num:
        print("Up")
    elif ANSWER < num:
        print("Down")
    else:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (5 - tries))
        break

    tries -= 1

print("아쉽습니다. 정답은 %d였습니다." % ANSWER)
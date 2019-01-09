import random

# 랜덤숫자 3개 리스트에 입력
numbers = []

number1 = random.randint(0, 9)

while True:
    number2 = random.randint(0, 9)
    if number2 == number1:
        continue
    else:
        break

while True:
    number3 = random.randint(0, 9)
    if number3 == number1 or number3 == number2:
        continue
    else:
        break

numbers.append(number1)
numbers.append(number2)
numbers.append(number3)

print(numbers)

# 사용자 숫자 3개 입력
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print()

print("세 수를 하나씩 차례대로 입력하세요.")
num1 = int(input("1번째 수를 입력하세요: "))

while True:
    num2 = int(input("2번째 수를 입력하세요: "))

    if num2 == num1:
        print("중복되는 수 입니다. 다시 입력해주세요.")

    else:
        break

while True:
    num3 = int(input("3번째 수를 입력하세요: "))

    if num3 == num1 or num3 == num2:
        print("중복되는 수 입니다. 다시 입력해주세요.")

    else:
        break

# 숫자 3개 리스트에 입력
guess = []
guess.append(num1)
guess.append(num2)
guess.append(num3)

print(guess)

# 스트라이크
i = 0
strike = 0

while i < 3:
    if numbers[i] == guess[i]:
        strike += 1
    i += 1

print("%dS" % strike)

# 보오올
i = 0
j = 0
ball = 0

while i < 3:
    while j < 3:
        if numbers[i] == guess[j]:
            ball += 1
        j += 1
    i += 1

print("%dB" % ball)
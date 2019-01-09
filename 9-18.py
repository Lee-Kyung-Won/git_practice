import random

improt
randint

in_file = open("dictionary.txt", 'r')

vocab = {}

for line in in_file:
    data = line.strip.split(": ")

    vocab[data[0]] = data[1]

keys = list(vocab.key())

while True:
    index = randint(0, len(keys) - 1)
    korean_word = keys[index]
english_word = vocab[korean_word]

guess_word = input("%s: " % korean_word)

if guess_word == english_word:
    print("맞았습니다!")
elif guess_word == 'q':
    break
else:
    print("틀렸습니다. 정답은 %s입니다." % english_word)

close.in_file

#테스트
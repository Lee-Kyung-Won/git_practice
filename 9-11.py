out_file = open('new_file.txt', 'w')

words = []

while True:
    english_word = input("영어 단어를 입력하세요: ")
    korean_word = input("한국어 뜻을 입력하세요: ")

    out_file.write("%s: %s\n" % (english_word, korean_word)

    if english_word or korean_word == "q":
        break

out_file.close
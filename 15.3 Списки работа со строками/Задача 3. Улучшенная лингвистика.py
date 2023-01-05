words_list = []
counts = [0, 0, 0]

for i in range(3):
    print("Введите", i+1, "слово", end=' ')
    word = input()
    words_list.append(word)

text = ''
while text != "end":
    text = input("Слово из текста: ")
    for index in range(3):
        if words_list[index] == text:
            counts[index] += 1
            #print(counts)

print("Подсчёт слов в тексте")
for i in range(3):
    print(words_list[i], ':', counts[i])
numbers_file = open('numbers.txt', 'r', )
summ = 0
for i_elem in numbers_file:
    summ += int(i_elem)
numbers_file.close()

answer_file = open('answer.txt', 'w')
answer_file.write(str(summ))
answer_file.close()
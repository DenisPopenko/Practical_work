# file = open('ages.txt', 'w')
# n = 3
# for i in range(10):
#     file.write(str(n) + '\n')
#     n += 7

file_read = open('ages.txt')
file_read.()
file_res = open('result.txt', 'w')
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# people = {}
# for i in file_read:
#     print(alpha.index(i))
#     # people[i] = file_read[alpha.index(i)]
#     print(i)
# print(people)
people = dict(zip(alpha, file_read))
print(people)
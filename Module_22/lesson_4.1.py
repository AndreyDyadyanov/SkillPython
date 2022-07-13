file = open('numbers.txt', 'r')

summ_count = 0

for number in file:
    summ_count += int(number)

file.close()

file_2 = open('answer.txt', 'w')
file_2.write(str(summ_count))
file_2.close()
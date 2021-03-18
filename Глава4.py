# char = ['w', 'a', 's', 'i', 't', 'a', 'r']
# out = ''
# length = len(char)
# i = 0
# while (i< length):
#     out = out +char[i]
#     i= i+1
# length = length * -1
# i=-2
# while (i >= length):
#     out = out + char[i]
#     i = i-1
# print(out)
# smothies = [1,2,3,4,5]
# length = len(smothies)
# for i in range(length):
#     print(i,smothies[i])

scores = [11, 20, 3, 4, 50, 20, 22, 60, 55, 22, 60]  # создаю список
costs = [.1, .20, .3, .4, .50, .20, .22, .60, .55, .22, .60]
high_score = 0  # создаю пустую перемен
best_sol = []  # создаю пустой список
length = len(scores)  # узнаю длину списка
cost = 100.0
most_effective = 0
for i in range(length):  # перебор списка
    print('раствор №', i, 'результат', scores[i])
if scores[i] > high_score:  # определение наиб значения
    high_score = scores[i]
for i in range(length):
    if high_score == scores[i]:
        best_sol.append(i)
for i in range(length):
    if scores[i] == high_score and costs[i]<cost:
        most_effective = i
        cost = costs[i]
print('всего тестов', length)
print('макс значение', high_score)
print('растворы с наиб результатом', best_sol)
print('самый лучший раствор', most_effective)
# for i in range (0, 4):
#     for j in range(0, 4):
#         print(i * j)
# for word in ['як', 'кот', 'пума', 'ягуар', 'собака', ]:
#     for i in range(2, 7):
#         letters = len(word)
#         if (letters % i) == 0:
#             print(i , word)
def bubble_sort(scores, numbers):  # пузырьковая сортировка
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(scores) - 1):
            if scores[i] < scores[i + 1]:
                temp = scores[i]
                scores[i] = scores[i + 1]
                scores[i + 1] = temp
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True


scores = [7, 11, 22, 3, 4, 5, 6, 2, 5, 666]
number_of_scores = len(scores)
solution_numbers = list(range(number_of_scores))
bubble_sort(scores, solution_numbers)
print(scores, solution_numbers)

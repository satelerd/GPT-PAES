

gpt_answers = ['A', 'B', 'D', 'B', 'D', 'D', 'C', 'C', 'D', 'D', 'B', 'B', 'A', 'C', 'D', 'C', 'A', 'D', 'D', 'A', 'A', 'A', 'C', 'C', 'C', 'D', 'D', 'B', 'A', 'D', 'B', 'B', 'C', 'C', 'B', 'A', 'B', 'A', 'B', 'D', 'D', 'D', 'C', 'D', 'B', 'D', 'D', 'A', 'B', 'C', 'A', 'B', 'A', 'B', 'D', 'A', 'C', 'D', 'A', 'C', 'B', 'D', 'A', 'A', 'A']
gpt_answers2 =['A', 'B', 'D', 'B', 'D', 'D', 'C', 'C', 'D', 'D', 'B', 'B', 'A', 'C', 'D', 'C', 'A', 'D', 'D', 'A', 'D', 'A', 'C', 'C', 'C', 'D', 'D', 'A', 'A', 'D', 'B', 'B', 'C', 'C', 'B', 'A', 'B', 'A', 'B', 'D', 'D', 'D', 'C', 'D', 'B', 'D', 'D', 'A', 'B', 'C', 'A', 'B', 'A', 'B', 'D', 'A', 'C', 'D', 'A', 'C', 'B', 'd', 'A', 'B', 'A'] #  , 'a', 'c', 'b']

real_answers =["A", "B", "C", "B", "D", "A", "C", "B", "B", "D", "B", "B", "A", "A", "D", "C", "D", "D", "D", "A", "B", "A", "C", "D", "C", "D", "B", "A", "A", "D", "B", "C", "D", "C", "C", "A", "B", "A", "B", "D", "D", "D", "C", "D", "B", "A", "D", "A", "C", "C", "A", "B", "A", "B", "D", "A", "C", "D", "A", "C", "B", "A", "A", "C", "A"]

correct = 0
incorrect = 0

for i in range(0, len(real_answers)):
    if gpt_answers2[i] == real_answers[i]:
        correct += 1
    else:
        incorrect += 1

print("Correct: ", correct)
print("Incorrect: ", incorrect)
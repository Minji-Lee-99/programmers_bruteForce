def solution(answers):
    len_ans = len(answers)
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [[1, 0], [2, 0], [3, 0]]

    for i in range(len_ans):
        if student1[i % 5] == answers[i]:
            count[0][1] += 1
        if student2[i % 8] == answers[i]:
            count[1][1] += 1
        if student3[i % 10] == answers[i]:
            count[2][1] += 1

    count.sort(reverse=True, key=lambda x: x[1])
    answer = []

    answer.append(count[0][0])
    for i in range(2):
        if count[i][1] == count[i+1][1]:
            answer.append(count[i+1][0])
        else:
            break

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))

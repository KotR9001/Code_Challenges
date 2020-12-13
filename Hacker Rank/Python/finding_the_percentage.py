if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

import decimal
if query_name in student_marks:
    #print(student_marks[query_name])
    avg = "{:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name]))
    print(avg)
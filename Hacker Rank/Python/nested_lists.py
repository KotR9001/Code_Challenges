if __name__ == '__main__':
    records = []
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        names.append(name)
        scores.append(score)

#print(records)
records.sort(key=lambda x: (x[1], x[0]))
#records.sort(key= lambda x: x[1])
unique_scores = []
for score in scores:
    if score not in unique_scores:
        unique_scores.append(score)
unique_scores.sort()
#print(unique_scores)

for e in records:
    if e[1] == unique_scores[1]:
        print(e[0])
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

score_list = []
for score in arr:
    score_list.append(score)

#print(score_list)
score_list.sort()
#print(score_list)
new_score_list = []
for score in score_list:
    if score not in new_score_list:
        new_score_list.append(score)
print(new_score_list[-2])
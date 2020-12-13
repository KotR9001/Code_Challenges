if __name__ == '__main__':
    n = int(input())
num_list = []
for i in range(1, n+1):
    i = str(i)
    num_list.append(i)
new_num_str = "".join(num_list)
new_num = int(new_num_str)
print(new_num)
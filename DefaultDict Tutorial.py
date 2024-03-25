# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
if __name__ == "__main__":
    n, m = map(int, input().split()) 
    group_a = defaultdict(list)
    for i in range(1, n + 1):
        word = input()
        group_a[word].append(i)
    for _ in range(m):
        word = input()
        if word in group_a:
            print(" ".join(map(str, group_a[word])))
        else:
            print(-1)

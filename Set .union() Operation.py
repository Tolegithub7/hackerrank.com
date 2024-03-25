# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
en = list(map(int, input().split()))
n2 = int(input())
fr = list(map(int, input().split()))
s1 = set(en)
s1 = s1.union(set(fr))
print(len(s1))

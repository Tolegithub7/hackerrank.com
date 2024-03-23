# Enter your code here. Read input from STDIN. Print output to STDOUT
t2 = int(input())
en = set(map(int, input().split()))
t2 = int(input())
fr = set(map(int, input().split()))
rs = en.difference(fr)
print(len(rs))

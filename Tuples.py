# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    lst = map(int, input().split())
    t = tuple(lst)
    print(hash(t))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    score = list(set(arr))
    score.sort(reverse=True)
    print(score[1])

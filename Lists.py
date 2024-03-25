if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        inst = input().split()
        if inst[0] == 'insert':
            lst.insert(int(inst[1]), int(inst[2]))
        elif inst[0] == 'print':
            print(lst)
        elif inst[0] == 'remove':
            lst.remove(int(inst[1]))
        elif inst[0] == 'append':
            lst.append(int(inst[1]))
        elif inst[0] == 'sort':
            lst.sort()
        elif inst[0] == 'pop':
            lst.pop()
        else: 
            lst.reverse()

# Enter your code here. Read input from STDIN. Print output to STDOUT
st = set(map(int, input().split()))
no = int(input())
ret = True
for i in range(no):
    st1 = set(map(int, input().split()))
    if not st.issuperset(st1) or st == st1:
        ret = False
        break
print(ret)

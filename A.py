T= int(input())

for i in range(T):
    x,y= map(int, input().split())
    if(x<y):
        print(f"{x} {y}")
    else:
        print(f"{y} {x}")
T= int(input())

for i in range(T):
    a,b,c,d= map(int, input().split())
    if(b<a):
        aux=b
        b=a
        a=aux

    if a<=c & c<=b  :
        if d>=b or d<=a:
            print("YES")
        else:
            print("NO")
    else:
        if(a<=d & d<=b):
            if(c>=b or c<=a):
                print("YES")
            else:
                print("NO");   
        else:
            print("NO")
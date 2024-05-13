T= int(input())

for i in range(T):
    palabra=input()
    if(len(palabra)==1):
        print("NO")
    else:
        letra=palabra[0]
        cambio=0
        j=1
        while(cambio==0 and j<len(palabra) ):
            if palabra[j]!=letra:
                cambio=1
                nuevo=palabra[j]+palabra[0:j]+palabra[j+1:len(palabra)]
            j+=1
        if cambio==1:
            print("YES")
            print(nuevo)
        else:
            print("NO")
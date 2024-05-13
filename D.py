T= int(input())



for i in range(T):
    cad=input()

    j=0
    hayCasoEspecial=0
    cantPiezas=1
    while j<len(cad):
        act=cad[j]
        while j<len(cad) and act==cad[j]:
            j+=1
        
        if(j<len(cad) and cad[j]=='1'):
            hayCasoEspecial=1
        
        if j<len(cad):
            cantPiezas+=1
        
    if hayCasoEspecial==1:
        print(cantPiezas-1)
    else:
        print(cantPiezas)
            



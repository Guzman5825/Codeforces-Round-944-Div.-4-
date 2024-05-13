#este no acepta, pero la idea es parecida aunque bueno, el que si acepta es de la carpeta E
def pos_menor_o_igual_a_x_BusqBin(v, x): #OJO MUY imporante x tiene que estar en el rango de valores de V
    l,r = -1,len(v)
    while r-l>1:
        m = (l+r)//2
        if v[m]>=x: r = m
        else: l = m
    if x==v[r]:    # si el numero existe en el vector, el unico que tendria su posicion es r
        return r
    return l    
 
T=int(input())
velocidades=[0]*(10**5+1)
a=[] #distancia
b=[] #tiempo
respuesta=""

for test in range(T):
    N,K,Q = map(int , input().split() ) #N=distancia total recorrida,K distancias que sabe timi, Q= consultas de timi
 
    a.clear()
    b.clear()
 
    a=[0]+list(map(int,input().split()))
    b=[0]+list(map(int,input().split()))
 
    for i in range(K):
        velocidades[i]=(a[i+1]-a[i])/(b[i+1]-b[i])
 
    for i in range(Q):
        qDistancia=int(input())
        pos=pos_menor_o_igual_a_x_BusqBin(a,qDistancia)
        if qDistancia==a[pos]:
            respuesta+=(str(b[pos]))+" "
        else:
            respuesta+=str(int(b[pos]+((qDistancia-a[pos])/velocidades[pos])))+" "
    
    if(len(respuesta)<=100000):
        respuesta+="\n"
    else:
        print(respuesta)
        respuesta=""
print(respuesta)
#include <bits/stdc++.h>

using namespace std;

int pos_menor_o_igual_a_x_BusqBin(int* v, int x,int tam) {
    int l = -1, r = tam;
    while (r - l > 1) {
        int m = (l + r) / 2;
        if (v[m] >= x)
            r = m;
        else
            l = m;
    }
    if (x == v[r]) { // si el número existe en el vector, el único que tendría su posición es r
        return r;
    }
    return l;
}


int main()
{
    cin.tie(0);
    cin.sync_with_stdio(0);

    int T,N,K,Q,qDistancia,pos,ia,ib;
    int a[100001];
    int b[100001];
    string res;

    cin>>T;

    a[0]=0;
    b[0]=0;

    for(int test=0;test<T;test++){
        cin>>N>>K>>Q;
        for(ia=1;ia<=K;ia++)
            cin>>a[ia];

        for(ib=1;ib<=K;ib++)
            cin>>b[ib];
        res="";

        for(int query=0;query<Q;query++){
            cin>>qDistancia;
            pos=pos_menor_o_igual_a_x_BusqBin(a,qDistancia,K+1);
            if( qDistancia==a[pos] )
                cout<<int(b[pos])<<" ";
            else
                cout<<b[pos]+((((qDistancia-a[pos])*(long long)((b[pos+1]-b[pos])))/(a[pos+1]-a[pos])))<<" ";
                //cout<<int(b[pos]+((qDistancia-a[pos])*((b[pos+1]-b[pos])/(long double)(a[pos+1]-a[pos]))))<<" ";
                //cout<<int(b[pos]+((qDistancia-a[pos])*((b[pos+1]-b[pos])/(long double)(a[pos+1]-a[pos]))))<<" ";
                //cout<<int(b[pos]+((qDistancia-a[pos])/((long double)(a[pos+1]-a[pos])/(b[pos+1]-b[pos]))))<<" ";
        }
        cout<<endl;
    }

    return 0;
}






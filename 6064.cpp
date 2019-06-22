#include <iostream>
#include <string>

using namespace std;

//최대공약수
int gcd(int a, int b){
    while(b!=0){
        int r = a%b;
        a=b;
        b=r;
    }
    return a;
}
//최소공배수
int lcm(int a, int b){
    return a*b/gcd(a,b);
}

int main(){

    // 시간이 너무 오래걸려서 OUT
    /*
        M N >= x,y
        <x:y>
        <1:1> 첫번재해
        <2:2> 두번째해
        <x:y> 다음해 <x':y'>
        x < M -> true : x' = x + 1 / false : x' = 1
        y < N -> true : y' = y + 1 / false : y' = 1
        final <M:N>

        10 12 3 9
        x%10 = 3 / 10+3=13 20+3=23 30+3=33
        x%12 = 9 / 12+9=21 24+9=33

        10 12 10 12
        20 30 40 50 60
        24 36 48 60
        final year = 최소공배수

        10 12 7 2
        17 27 37 47 57 67 77 87
        14 26 38 50 62 74 86 98

        13 11 5 6
        13+5=18 31 44 57 70 83
        11+6=17 28 39 50 61 72 83

        (M+x)+M*i == (N+y)+N*j

    */
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int k;
    cin >> k;

    int M[k], N[k], x[k], y[k], r[k];

    for(int i=0; i<k; i++){
        cin >> M[i] >> N[i] >> x[i] >> y[i];
    }

    for(int i=0; i<k; i++){

        long ll = lcm(M[i], N[i]); //1:60
        int mx = M[i]+x[i];
        int ny = N[i]+y[i];
        r[i] = -1;

        for(int j=0; j<ll/M[i]; j++){
            for(int m=0; m<ll/N[i]; m++){
                if(mx+(M[i]*j) == ny+(N[i]*m)){
                    r[i] = mx+(M[i]*j);
                }
            }
        }
        cout << r[i] << "\n";
    }

    return 0;
}

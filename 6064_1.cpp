#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int gcd(int a, int b){
    while(b!=0){
        int r = a%b;
        a=b;
        b=r;
    }
    return a;
}
int lcm(int a, int b){
    return a*b/gcd(a,b);
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int m, n, x, y, i, j, k;
    cin >> k;

    for(i=0; i<k; i++){
        cin >> m >> n >> x >> y;

        int maxi = lcm(m, n);

        for(j=x; j<=maxi; j+=m){
            int temp = (j%n == 0) ? n : j%n;
            if(temp == y) {
                cout << j << "\n";
                break;
            }
        }
        if(j>maxi) cout << "-1\n";
    }

    return 0;
}

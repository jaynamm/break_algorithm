#include <iostream>

using namespace std;

int main(){
    int n;
    int cnt=0;
    int tmp;

    cin >> n;

    tmp = n;

    while(true){
        tmp = 10*(tmp%10) + (tmp/10 + tmp%10)%10;
        cnt++;

        if(tmp == n){
            cout << cnt << "\n";
            break;
        }
    }

    return 0;
}

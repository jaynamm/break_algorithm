#include <iostream>

using namespace std;

int d(int n){
    int sum = n;

    while(n!=0) {
        sum += n%10;
        n = n/10;
    }

    return sum;
}

int main(){

    bool arr[10001];
    int tmp;

    for(int i=1; i<=10000; i++){
        arr[i] = true;
    }

    for(int i=1; i<=10000; i++){
        tmp = d(i);
        if(tmp <= 10000) {
            arr[tmp] = false;
        }
    }

    for(int i=1; i<=10000; i++) {
        if(arr[i]) {
            cout << i << "\n";
        }
    }

    return 0;
}

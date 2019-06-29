#include <iostream>

using namespace std;

int main(){
    int n, x;

    cin >> n >> x;

    int a[n+1];

    for(int i=0; i<n; i++){
        cin >> a[i];

        if(a[i] < x){
            cout << a[i] << " ";
        }
    }

    return 0;
}


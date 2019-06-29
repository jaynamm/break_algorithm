#include <iostream>

using namespace std;

int main(){
    int n;
    int tmp;

    cin >> n;

    int num[n+1];
    for(int i=0; i<n; i++){
        cin >> num[i];
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(num[i] < num[j]){
                tmp = num[i];
                num[i] = num[j];
                num[j] = tmp;
            }
        }
    }

    for(int i=0; i<n; i++){
        cout << num[i] << "\n";
    }

    return 0;
}

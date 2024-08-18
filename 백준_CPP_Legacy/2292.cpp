#include <iostream>

using namespace std;

int main() {
    /*
         1    : 1
         2-7  : 2
         8-19 : 3
        20-37 : 4
        38-61 : 5
    */

    int n;
    int i=1;

    cin >> n;

    int before = i;
    int after;

    if(n == 1) {
        cout << "1" << "\n";
        return 0;
    } else {
        while(true){
        after = before + 6*i;

        if(before<n && n<=after){
            cout << i+1 << "\n";
            return 0;
        }
        before = after;
        i++;
    }
    }
}

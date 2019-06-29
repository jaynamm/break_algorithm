#include <iostream>

using namespace std;

int main(){
    int a, b, c;

    cin >> a >> b >> c;

    if(a >= b && a >= c){
        if(b >= c){
            cout << b << "\n";
        } else{
            cout << c << "\n";
        }
    } else if(b >= a && b >= c){
        if(a >= c){
            cout << a << "\n";
        } else {
            cout << c << "\n";
        }
    } else if(c >= a && c >= b){
        if(a >= b){
            cout << a << "\n";
        } else{
            cout << b << "\n";
        }
    }

    return 0;
}


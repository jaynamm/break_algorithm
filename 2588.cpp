#include <iostream>

using namespace std;

int main(){

    int num1, num2;
    int tmp, res;

    cin >> num1 >> num2;

    tmp = num2;

    while(tmp>0){
        res = tmp%10;
        cout << num1*res << "\n";
        tmp = tmp/10;
    }

    cout << num1*num2 << "\n";

    return 0;
}


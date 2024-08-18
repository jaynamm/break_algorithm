#include <iostream>
#include <stdio.h>

using namespace std;

int main() {

    int n, tmp;
    char num;
    int sum=0;
    cin >> n;

    for(int i=1; i<=n; i++){
        cin >> num;
        tmp = num - '0';
        sum += tmp;
    }

    cout << sum << "\n";

    return 0;
}

#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main() {

    int t, a, b;
    int sum = 0;
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> t;

    for(int i=0; i<t; i++){
        cin >> a >> b;
        sum = a+b;
        cout << sum << "\n";
    }

    return 0;
}

#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main() {

    string s;

    getline(cin, s);

    for(int i=0; i<s.size(); i++){
        cout << s[i];
        if((i+1)%10==0) cout << "\n";
    }

    return 0;
}

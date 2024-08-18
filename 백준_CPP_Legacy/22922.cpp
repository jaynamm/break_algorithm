
#include <iostream>

using namespace std;

int main() {
    /*
         1    : 1    1
         2-7  : 2    (n-1)+6*1
         8-19 : 3    (n-1)+6*2
        20-37 : 4    (n-1)+6*3
        38-61 : 5    (n-1)+6*4
        .
        .
    */

    int n;
    int i=1;
    cin >> n;

    while(true) {
        int before = 1+(6*(i-1));
        int after = before + (6*i);

        cout << before << " / " << after << "\n";

        if(before < n && n <= after) {
            cout << i+1 << "\n";
            return 0;
        }
        i++;
    }
}

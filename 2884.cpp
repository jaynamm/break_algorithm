#include <iostream>

using namespace std;

int main(){
    int h, m;
    int hh, mm;

    cin >> h >> m;

    if(m < 45){
        if(h < 1) hh = 23;
        else hh = h -1;

        mm = 60 + (m - 45);

        cout << hh << " " << mm << "\n";
    } else {
        hh = h;
        mm = m - 45;

        cout << hh << " " << mm << "\n";
    }

    return 0;
}


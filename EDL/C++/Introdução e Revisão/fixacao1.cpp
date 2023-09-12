#include <iostream>
using namespace std;

void misterio(int *p, int *q){
    int temp;
    temp = *p;
    *p = *q;
    *q = temp;
}

int main(){
    int i=6;
    int j=10;

    misterio(&i, &j);

    cout << i << endl;
    cout << j << endl;

    return 0;
}
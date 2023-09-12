#include <iostream>
using namespace std;

int main(){
    int i=99, j;
    int *p;
    p=&i;
    j=*p+100;
    cout << i << endl;
    cout << j << endl;
    return 0;
}
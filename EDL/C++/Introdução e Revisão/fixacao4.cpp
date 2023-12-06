#include <iostream>
using namespace std;

int main(){
    int i=7, j=3, c;
    int *p;
    int **r;
    p = &i;
    r = &p;
    c = **r + j;
    cout << c << endl;
    return 0;
}
// #include <iostream>
// using namespace std;
// #include <cstring>

// int main(){

//     string nome = "teste";

//     int tam = nome.size();

//     cout << tam << endl;


// return 0;
// }

#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s;
    getline(cin, s);
    for(int i=0; i<s.length();i++)
    {
        cout << s.at(i) << endl;
    }
   
    return 0;
}
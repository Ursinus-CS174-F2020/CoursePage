#include <iostream> 
#include <iterator> 
#include <map> 
using namespace std;

int main() {
    map<string, string> mymap;
    mymap.insert(pair<string, string>("Chris", "A postdoc at Duke"));
    mymap.insert(pair<string, string>("Professor Schilling", "Ursinus instructor"));
    mymap.insert(pair<string, string>("Barack Obama", "44th US President"));
    cout << (mymap.find("Chris") != mymap.end()) << "\n"; //Prints "1"
    cout << mymap["Chris"] << "\n"; //Prints "A postdoc at Duke"
    mymap.erase("Chris");
    cout << (mymap.find("Chris") != mymap.end()) << "\n"; //Prints "0"
    return 0;
}

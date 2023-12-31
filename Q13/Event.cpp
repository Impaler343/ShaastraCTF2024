#include <iostream>
#include <string>

using namespace std;

int main() {
    cout<<"Enter a string\n";
    string s;
    cin>>s;
    for(int i=0; i<s.size(); i++){
        s[i]=tolower(s[i]);
    }
    while(s!="ctf") {
        cout<<"Try Again!\n";
        cin>>s;
        for(int i=0; i<s.size(); i++){
        s[i]=tolower(s[i]);
    }
    }
    cout <<"The third part of flag is:- \n_Y34R!}\n";
    while(1);
    // return 0;
}
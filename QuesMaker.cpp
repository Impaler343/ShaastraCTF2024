#include <bits/stdc++.h>
using namespace std;

string toBin(char c){
    int n=c;
    string s="";
    while(n!=0){
        if(n%2) s="1"+s;
        else s="0"+s;
        n/=2;
    }
    for(int i=s.size(); i<8; i++){
        s="0"+s;
    }
    return s;
}
int main() {
    // The flag
    string s="Y35_7h15_I5_7h3_FL4G";
    
    //Ascii value in of the characters in binary, each 8 bits
    string s1="";
    for(int i=0; i<s.size(); i++){
        s1+=toBin(s[i]);
    }
    // s1.size() == 160

    string s2="iamtwoboredoffindingflagsiwanttwodosomethingmoreinterestingwaitdidyouseethattwonoyoudidnotijustfoundtheflagnowiamgoingtwothenextquestionyoucanalsogoifyouwishtwo";
    // s2.size() == 160
    
    for(int i=0; i<s2.size(); i++){
        if(s1[i]=='1') s2[i]=toupper(s2[i]);
        else s2[i]=tolower(s2[i]);
    }
    // cout<<s2<<endl;
    // s2 == "iAmTWobOreDOffINdiNGfLaGsIwANTTWodOSoMEThINgMoreinTEresTinGWaItDiDyOUSEEtHatTwoNoyOUdIdNoTiJUSTFouNDtHEFlAGnOwiamgOIngTWoThENEXTqUestIOnyOucANalsoGOiFyouWishTWO"
}
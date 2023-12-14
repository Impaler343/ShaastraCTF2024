#include <bits/stdc++.h>
using namespace std;

int main() {
    string s="iAmTWobOreDOffINdiNGfLaGsIwANTTWodOSoMEThINgMoreinTEresTinGWaItDiDyOUSEEtHatTwoNoyOUdIdNoTiJUSTFouNDtHEFlAGnOwiamgOIngTWoThENEXTqUestIOnyOucANalsoGOiFyouWishTWO";
    
    int k=s.size();
    string flag="";
    for(int i=0; i<k; i+=8){
        int ans=0;
        for(int j=i; j<i+8; j++){
            ans<<=1;
            if(s[j]>='A'&&s[j]<='Z') ans++;
        }
        char c=ans;
        flag+=c;
    }
    cout<<flag<<endl;
}
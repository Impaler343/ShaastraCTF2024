#include <bits/stdc++.h>
using namespace std;

int main() {
    string s="IaMBorEdOFfiNDiNGfLaGSiWANTTwODoSOMEthInginTEresTiNGwAiTDiDYOUSeEThatTwONoYoUDiDNOTIjUStFOUNdtHeflaGIamGOInGTWOTHeneXTqUesTIonyOUtWocAngoNOW";
    
    int k=s.size();
    string flag="";
    for(int i=0; i<k; i+=7){
        int ans=0;
        for(int j=i; j<i+7; j++){
            ans<<=1;
            if(s[j]>='A'&&s[j]<='Z') ans++;
        }
        char c=ans;
        flag+=c;
    }
    cout<<flag<<endl;
}
#include <iostream>
using namespace std;
    

string pw = "ShaastraCTF{dLkDF@^HgsGRus63EsT&}";
string val = "0";
int ans = -255;
string s;

bool check_number(string str){
    int x = 0;
    if(str[0] == '-')x = 1;
    if(str.size() > 10+x || str.size() == 0) return false;
   for (int i = x; i < str.length(); i++){
   if(isdigit(str[i]) == false)
      return false;
   }
   return true;
}

string response(int val){
    int diff = abs(val-ans);
    if(diff == 0) return "";
    else if(diff < 5) return "Single digit on kelvin scale";
    else if(diff < 10) return "freezing";
    else if(diff < 25) return "very cold";
    else if(diff < 50) return "cold";
    else if(diff < 100) return "cool";
    else if(diff < 200) return "warm";
    else if(diff < 300) return "hot";
    else if(diff < 500) return "burning";
    else return "You are on the sun";
}
int main(){
    while(stoi(val) != ans){
    cout <<"Enter guess\n";
    getline(cin,val);
    if(check_number(val)){
    cout << response(stoi(val)) << "\n";
    }
    else{ cout << "Please enter a valid number within limits of int\n";
    val = "0";
     }
    }
    cout << pw << "\n";
}


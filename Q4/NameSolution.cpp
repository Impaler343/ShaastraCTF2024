#include <bits/stdc++.h>
#define ll long long

using namespace std;
ll counter = -1;
ll fibbmod(ll n){
    counter ++;
    if(n == 0) return 2;
    else if(n == 1) return 3;
    cout << counter << " " << n << "\n";
    if(counter%2){
        return fibbmod(n-1) - fibbmod(n-2);
    }
    else{
        return fibbmod(n-1) + 2*fibbmod(n-2);
    }
}

int main() {
    ll n = 250;
    vector<ll> odd = {2,3},even = {2,3};
    for(ll i = 2;i<=n;i++){
        odd.push_back(even[i-1] - odd[i-2]);
        even.push_back(odd[i-1] + 2*even[i-2]);
    }
    if(true){
        for(ll i = 0; i <=n;i++){
            cout << odd[i] << " " << even[i] << "\n";
        }
    }
    else{
        cout << even[n] << "\n";
    }
    return 0;
}

// 0->2
// 1->3
// 2->7
// 3->7
// 4->18
// 5->20
// 6->50
// 7->54
// 8->136
// 9->148
// 10->372
// 11->404
// 12->1016
// 13->1104
// 14->2776
// 15->3016
// 16->7584
// 17->8240
// 18->20720
// 19->22512
// 20->56608
// 21->61504
// 22->154656
// 23->168032
// 24->422528
// 25->459072
// 26->1154368
// 27->1254208
// 28->3153792
// 29->3426560

// 250->4611686018427387904
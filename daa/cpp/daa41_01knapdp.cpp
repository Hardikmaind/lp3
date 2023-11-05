#include<bits/stdc++.h>
using namespace std;

int knapsack(int W, int wt[], int val[], int n) {
    int dp[W + 1];
    memset(dp, 0, sizeof(dp));

    for(int i=1; i<=n; i++){
        for(int j=W; j>=0; j--){
            if(wt[i-1]<=j){
                dp[j]= max(dp[j], dp[j]-wt[i-1]+val[i-1]);
            }
        }
    }
    return dp[W];
}

int main() {
    int W;
    cout << "Enter capacity of Knapsack: ";
    cin >> W;

    int n;
    cout << "Enter Number of Items: ";
    cin >> n;

    int *wt = new int[n];
    int *val = new int[n];

    for (int i = 0; i < n; i++) {
        cout << "Enter value and weight of Item " << i + 1 << ": ";
        cin >> val[i] >> wt[i];
    }

    cout << "Maximum Value in knapsack: " << knapsack(W, wt, val, n);

    return 0;
}
// 50 3 60 10 100 20 120 30
//TC - O(W*n)
//S - O(n)
#include<bits/stdc++.h>
using namespace std;

struct Item{
    int Profit;
    int Weight;
};

static bool cmp( struct Item a, struct Item b){
    double r1 = (double)a.Profit/(double)a.Weight;
    double r2 = (double)b.Profit/(double)b.Weight;

    return r1>r2;
}

double fractionalknapsack(int W, struct Item arr[], int N){

    sort(arr, arr+N, cmp);
    double FinalValue=0.0;
    for(int i=0; i<N; i++){
        if(arr[i].Weight<W){
            W-=arr[i].Weight;
            FinalValue+= arr[i].Profit;
        }
         else{
        FinalValue+= arr[i].Profit*((double)W/(double)arr[i].Weight);
        }
    }

    return FinalValue;

}

int main(){
    int W;
    cout<<"Enter capacity of Knapsack: ";
    cin>>W;

    int N;
    cout<<"Enter Number of Items: ";
    cin>>N;

    Item arr[N];

    for(int i=0; i<N; i++){
        cout<<"Enter Profit and weight for Item"<<i+1<<":";
        cin>>arr[i].Profit>>arr[i].Weight;
    }
    cout<<"Maximum Value in knapsack: "<<fractionalknapsack(W,arr,N);
}
// 50 3 60 10 100 20 120 30
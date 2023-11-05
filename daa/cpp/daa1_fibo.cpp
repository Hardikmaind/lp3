#include <iostream>
using namespace std;


//Recursive
int fiboRecursive(int n)
{
    if(n==0){
        return 0;
    }
    if(n==1){
        return 1;
    }

    int a = fiboRecursive(n-1);
    int b = fiboRecursive(n-2);
    return a + b;
}

//Iterative

int fiboIterative(int n){

    int a=0,b=1,c,i;

    if(n<=1) return n;

    for(i=2; i<=n; i++){
        c= a+b;
        a=b;
        b=c;
    }
    return b;
}

int main(){
   while(true){
    cout<<"Fibonacci series menu: "<<endl;
    cout<<"1.Recursive"<<endl;
    cout<<"2.Iterative"<<endl;
    cout<<"3.Exit"<<endl;
    int choice=0;
    cout<<"Enter Choice(1/2/3): ";
    cin>>choice;
    int n;

    if(choice==1){
        cout<<"Enter n: ";
        cin>>n;
        cout<<n<<"th fibonacci number is: "<<fiboRecursive(n)<<endl;
        cout<<endl;
    }

    else if(choice==2){
        cout<<"Enter n: ";
        cin>>n;
        cout<<n<<"th fibonacci number is: "<<fiboIterative(n)<<endl;
        cout<<endl;
    }

    else if(choice==3){
        cout<<"Goodbye";
        break;
    }
   }
   return 0;
}
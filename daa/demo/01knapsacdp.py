def main():
    while True:
        print("o-1 knapsack problem solver")
        print("1. calculate maximum rpfit for a custom set of values")
        print("2.exit")
        choice=int(input("enter your choice"))
        if choice==1:
            n=int(input("enter the number of items"))
            val=list(map(int,input("enter the values of items" ).split()))
            wt=list(map(int,input("enter the weight of items" ).split()))
            W=int(input("enter the knapsack capactiy"))
            if len(val)!=n and len(wt)!=n:
                
                continue
            print("max possibel " ,knapsackdp(W,wt,val,n))
            
            

def knapsackdp(W,wt,val,n):
    K=[[0 for x in range(W+1)] for x in range (n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w]=0
            elif wt[i-1]<=w:
                K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
                
    return K[n][W]



if __name__=="__main__":
    main()
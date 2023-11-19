class ItemValue:
    def __init__(self,wt,val,ind):
        self.wt=wt
        self.val=val
        self.ind=ind
        self.cost=val//wt
    def __lt__(self,other):
        return self.cost<other.cost
    

def fracKnapsack(wt,val,capacity):
    # jitene wt hain utne objects initailize kiye
    ival=[ItemValue(wt[i],val[i],i) for i in range(len(wt))]
    ival.sort(key= lambda x:x.cost,reverse=True)
    totalval=0
    for i in ival:
        curwt=i.wt
        currval=i.val
        if capacity-curwt>=0:
            capacity-=curwt
            totalval+=currval
        else:
            fraction=capacity/curwt
            totalval+=currval*fraction
            capacity=int(capacity-(curwt*fraction))
            break
    return totalval


def main():
    while True:
        print("menu:")
        print("1. calculucate the maximum value in knapsack")
        print("2.exit")
        choice=int(input("enter your choice"))
        if choice==1:
            wt=list(map(int,input("enter the wrights separated by spaces : ").split()))
            val=list(map(int,input("enter the values seperated by spaces: ").split()))
            capacity=int(input("enter the capacity of the knapasck"))
            
            maximumValue=fracKnapsack(wt,val,capacity)
            print("max value in knapsack is", maximumValue)
        elif choice==2:
            break
        else:
            print("invalid input entered")
            
            
if __name__=="__main__":
    main()


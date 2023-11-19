def fibo(n,count):
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        count=count+1
    print(f"and the step count is : {count}")

    return fib[n]

def fibonacci_recursive(n):
    if n==1:
        return 1
    if n==0:
        return 0;
    fib_recur[n]=fibonacci_recursive(n-1)+ fibonacci_recursive(n-2)
    return fib_recur[n]
    

while True:
    print("Menu:")
    print("1. Calculate Fibonacci (Non-Recursive)")
    print("2. Calculate Fibonacci (Recursive)")
    print("3. Quit")
    choice = int(input("Enter your choice (1/2/3): "))
    if choice==1:
        count=0
        n=int(input("please enter the number: "))
        fib=[0]*(n+1)
        fib[1]=1
        result=fibo(n,count)
        print(f"this is the number {result}")
        print("time complexity of the code is O(n) and space complexity is (1)")
    elif choice==2:
        n=int(input("please enter the number: "))
        fib_recur=[0]*(n+1)
        fib_recur[1]=1
        result=fibonacci_recursive(n)
        print(f"this is the number {result}")
        print("time completxity of the code is O(2^n) and space complexity is O(n)")
    elif choice==3:
        print("you have exited from the program: ")
        break
    else:
        print("invalid input")
        
        
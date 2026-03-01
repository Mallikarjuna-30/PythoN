#<----- Fibonacci Series ----->#

def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
    
n = 5
for i in range(n+1):
    print(fib(i),end=" ")
    

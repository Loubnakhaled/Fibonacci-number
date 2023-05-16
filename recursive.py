import time #this module is imported to calculate the execution time of the code 
import sys  #this module is imported to increase the recursion limit to attend the needed number

sys.setrecursionlimit(13000)
def F(n):
    if n == 0 or n == 1: #given that F(0)=0 and F(1)=1 so we can just return n
        return n
    else:
        return F(n - 1) + F(n - 2) #this function will call itself two times 


start_time = time.time()
print(F(10)) #here the nth number is chosen 
end_time = time.time()
execution_time = end_time - start_time #execution time is calculated using the time function before and after calling the recursive function F(n)
print("Execution Time:", execution_time, "seconds") #show the execution time to analyse the time complexity of the code 

#results required
#F(0)=0
#F(1)=1
#F(2)=1 
#F(3)=2
#F(10)=55 
"""concerning the time complexity analysis, let's break down the function into steps or a tree:
For F(n), it makes two recursive calls: F(n-1) and F(n-2).
For F(n-1), it makes two recursive calls: F(n-2) and F(n-3).
For F(n-2), it makes two recursive calls: F(n-3) and F(n-4).
This pattern continues until we reach the base cases of F(0) and F(1), where no further recursive calls are made.
we can observe that the height of the tree is approximately n, and each level branches into two recursive calls.
The total number of nodes is roughly 2^n. Each node represents a recursive call, and as a result, the time complexity of the code is exponential.
so O(2^n) As n increases, the time required to calculate the Fibonacci number grows exponentially which makes it unefficient for larger numbers, will took soo long.
F(30)=0.17220091819763184 s
F(31)=0.296405553817749 s
F(35)=1.8882064819335938 s
F(36)=3.0573530197143555 s
F(40)=20.774508476257324 s
and by increasing n the time gets way larger"""

import time, sys

#### Run via command line with your desired Fibonacci number ####
#
# i.e python3 fib.py 15
# 

def recurFib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return recurFib(num - 1) + recurFib(num - 2)

def forFib(num):
    fibList = [0,1,1]
    for x in range(3, num+1):
        fibList.append(fibList[x-1] + fibList[x-2])
    
    return fibList[num]    


fibOfN = int(sys.argv[1])
start = 0
end = 0

start = time.perf_counter()
if sys.argv[2] == 'recur':
    answer = recurFib(fibOfN)
elif sys.argv[2] == 'loop':
    answer = forFib(fibOfN)
end = time.perf_counter()

total = format(end - start, '.6f') 

print("Fib of "+ str(fibOfN) + " is " + str(answer)+ " took "+ str(total) + " seconds") 


import math
import random
import time



def IsPrime(x):
    s= int(math.sqrt(x))
    for i in range(2,s+1):
        if x%i==0:
            return False
    return True

#millers test according to the book. let n be a positive 
#integer and let n - 1 = 2^s*t, where s is a nonnegative
#integer and t is an odd positive integer. We say that n passes
#millers test if either b^t =1(modn) or b**2**j*t = -1 (modn)

#examples of millers test from class

#n = 101
#n - 1 = 100 = 2**s*t
            #=2**2*25   s is # of 2 which can be divided until an odd number occurs
            #s = 2
            #where t is an odd positive integer in this case t = 25
#first method to see if a number passes millers test is b**t%n=1
    #b must be a random between 2 and n-1
        #in this instance b = 2
            #2**25%101 = 10 therefore this test is not true.
#second method involves using a variable named j
    #j = loops go from 0 to s-1
        # j = 0  b**j**t%n = n-1
            #2**25%101 = 10 therefore this test is not true
        # j = 1 b**j**t%n = n-1
            #2**50%101 = 100 therefore this test IS TRUE

def Millerstest(num):
    N = int(num)
    s = 0
    t = N-1
    while t%2==0:
        t=t//2
        s+=1
    #quotient remainder theorem
    #A = B * Q + R
    #example a = 7,b = 2
    # 7 = 2 * 3 + 1
    # 7 mod 2 = 1 

    B = random.randint(2,N-1)
    mB = pow(B,t,N)
    if mB == 1:
         return True
    J = 0
    while J != s:
        JT = 2**J*t
        mJ = pow(B,JT,N)
        if mJ == N-1:
            return True
        J += 1
    return False
        

def isprimemiller(num):
    reps = 10
    for i in range(0,reps):
        ok = Millerstest(num)
        if ok != True:
            return False
    return True
    






        

def main():
    start = time.time()
    for i in range(2,1000000):
        if i%2 != 0:
            if IsPrime(i) != isprimemiller(i):
                print("Error one or both or i maybe wrong")
    end = time.time()
    print("Time taken:",end-start,"Seconds")




    

main()
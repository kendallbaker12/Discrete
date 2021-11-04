import math
import random



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
    print(isprimemiller(831803604619031383835780666047))
    print(isprimemiller(951051464014810226123241868379))
    print(isprimemiller(969985062055950008331567304291))
    print(isprimemiller(969985062055950008331567304297))
    print(isprimemiller(10430085183478195189645936757800970661490851361791745025771984385316233372143768737102412177181789673235855492074381997692689504104210921247436919156668948180565177435050332809810225258982720046815821))
    print(isprimemiller(40386583886377437483326391813800188372680352926535839460633025082734576745096642373836365455339477673687068280985557629216935569))
main()
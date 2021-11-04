from math import factorial

 
def permutations(s):
    
    mSeq = list(s)
 
    for point in range(factorial(len(mSeq))):
        print(''.join(mSeq))
 
        point = len(mSeq) - 1
        while point > 0 and mSeq[point - 1] > mSeq[point]:
            point -= 1
 
        mSeq[point:] = reversed(mSeq[point:])
        
 
        if point > 0:
            q = point
            while mSeq[point - 1] > mSeq[q]:
                q += 1
 
            mSeq[point - 1], mSeq[q] = mSeq[q], mSeq[point - 1]
 
def main():
    s = input("Enter a range of numbers between 1-9: ")
    print(permutations(s))


main()
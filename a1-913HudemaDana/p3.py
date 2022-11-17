#problem 14


from math import *


#check if a number is prime
def prim(a:int):
    if a > 1:
        for i in range(2, int(sqrt(a))+1):
            if int(a % i) == 0:
                return False
        return True
    else:
        return False

#find prime divisors and add them to the sum
def divp(n:int):
    if prim(n):
        return 1

    nr=0
    for i in range(2,n-1):
        if (int(n%i)==0) and (prim(i) == True):
               nr=nr+i
    return nr

#knowing the last number
def solution(n,k):
    d,p,nr=2,0,0
    while n>1:
        while int(n%d)==0:
            n=n/d
            p=p+1
        if p:
            nr=nr+d
            if nr>=k:
                return d
        d=d+1
        p=0
    return 0


def main():
    #read numbers
    n= int(input())
    th=int(input())

    nr,i,ok=0,1,1

    #generate the sequence and find the element
    while(ok):
        if(nr+divp(i)) < (n-th):
            nr=nr+divp(i)
        else:
            if solution(i,n-th-nr) == 0:
                print(i)
            else:
                print(solution(i,n-th-nr))
            ok=0
        i=i+1


main()
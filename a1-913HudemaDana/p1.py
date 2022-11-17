#problem 2


from math import *

#verify if the numbers are prime
def prime(a:int):
    if a > 1:
        for i in range(2, int(sqrt(a))+1):
            if int(a % i) == 0:
                return False
        return True
    else:
        return False


#read the variable and check the required condition
def main():
    n = int(input())
    for i in range(2, n//2):
        if (prime(i) == True) and (prime(n-i) == True):
            print(i, " ", n-i)


main()
"""
You are given 2 arrays of size N and M respectively and a number X you have to tell that how many pairs of array A[i] and B[j] exists such that product of them will the co-prime of X.

 Input:
First Line contains 3 integers N,M,X
next line will contain N space seperated Integers.
next line will contain M space seperated Integers.


Output:
A single line no of such pairs.

Constraints:

SubTask 1 (30 Marks)
1<= N,M,X <=100
1 <= A[i],B[i] <= 10


Subtask 2 (70 Marks)
1 <= N,M,X <= 105
1 <= A[i],B[i] <= 106


Sample Input:
2 2 4
1 3
5 2

Sample Output:
2

Explaination:

1*5=5,4 -> co-primes
1*2=2,4 -> not co-primes
3*5=15,4 -> co-primes
3*2=6,4 -> not co-primes

So, ans is 2
"""

def primefactors(num):
    factorset=set()
    if(num==1):
        return set()
    while(True):
        limit=int(pow(num,0.5))
        for i in range(2,limit+1):
            if(num%i==0):
                factorset.add(i)
                #factorset.add(num//i)
                num=num//i
                break
        else:
            factorset.add(num)
            break
    return factorset


N,M,X=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
# find all the primefactors of X..
s=primefactors(X)
count=0
flag=0
for i in arr1:
    s1=primefactors(i)
    if(not s1.intersection((s))):
        count+=1
for i in arr2:
    s1=primefactors(i)
    if(not s1.intersection((s))):
        flag+=1

print(count*flag)


# complexity ananlysis :-
# avg complexity of primefactors in logn
# worst case sqrt(n)
# so worst case complexity :- n(n**0.5) avg nlogn


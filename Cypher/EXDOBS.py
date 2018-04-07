"""
All submissions for this problem are available.$Scube$ tried whole night to make a question but he was unable to make any good question,
 so he decided to extend the question $"Obsession"$ asked in the previous round.In that question, you had to make the numbers using $1$ and $0$ only.
 Here you will be given a number $N$ and a digit $K$ and you have you find the smallest multiple of $N$ that consists only of digit $K$ and $0$.
"""

""" Test Cases :
    5 2  => 20
    7 4  => 4004
    13 7 => 7007
"""

def my_gcd(m,n):
    if(m<n):
        m,n=n,m
    while(n!=0):
        temp=m
        m=n
        n=temp%n
    return m

def dec_to_binary(num,base=2):
    ans=""
    if(num==0):
        return "0"
    while(num!=0):
        rem=num%base
        num=num//base
        ans=ans+str(rem)
    return ans[::-1]


from math import *
n,m=map(int,input().split())
n=n//gcd(n,m)
i=1
while(True):
    x=bin(i)
    x=x[2:]
    if(int(x)%n==0):
        print(int(x)*m)
        break
    i+=1


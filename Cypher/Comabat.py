#https://www.codechef.com/CAD32018/problems/DBZ1
"""
Tournament of power is being held and GOKU is leader of his team having N members.He have to face team from other universe having M members .
You are given combat powers of members of team goku and combat powers of members of there opposition team.
if two fighters fights the fighter with greater power wins. if they have same power it is a draw.


GOKU wants to choose M of his fighters and make each of them fight with one of other team fighters.
Obviously, GOKU wants to win all the M fights. In every fight, the two FIGHTERS get hurt, and cannot fight again no matter who wins.
GOKU is worried about this, because he wants to be as prepared as possible for other future teams.
If there are more possibilities of winning all the M fights, GOKU is interested in maximizing the sum of CP of all the other N-M fighters that he doesn't choose in this fight. Your task is to help GOKU.



NOTE : Each of the goku fighter should win the individuals fight to win the complete COMBAT
"""

""" Test Cases :
Input 1:
2 2
5 9
1 4 
Output :- 0
Input 2: 4 3
10 1 7 5
5 2 11
Output :- -1

Input 3: 6 3
4 6 9 10 14 17
4 7 9

OutPut:-35

"""
n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
if(n<m):
    print("-1")
else:
    # it is ensured that n is greater than or equal to  m
    A.sort(reverse=True)    #N log N
    B.sort(reverse=True)    
    # Both A and B are sorted in reverse order..
    #i.e A=[17,14,10,9,6,4] and B=[9,7,4]
    # N and M are of Different Sizes..
    for i in range(m):
        if(B[i] >=A[i]):
            print("-1")
            break
    else:
        # it is guerrented that A will win..
        # that is answer will sum of (N-M) elements
        if(n==m):
            print("0")
        else:
            while(B):
                item=B[-1]
                # search this item from end Of A
                count=0
                for i in reversed(A): #M*N it seems .. but actually it only max N
                    if(i<=item):
                        count=count+1
                        ans+=i
                    else:
                        break
                else:
                    print("0")
                A=A[0:n-count]
                A=A[0:-1]
                n=n-count
                B=B[0:-1]
                #print(A,B,item,count)
            print(ans+sum(A))


# complexity analysis:-
    #O( NlogN + MlogM + N)

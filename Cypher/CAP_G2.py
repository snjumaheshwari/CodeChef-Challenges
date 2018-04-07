# CAP_G2

"""Cypher team is playing a game in which there are 3 buckets and each bucket have A, B and C number of balls respectively
that are numbered from 1 to A, 1 to B and 1 to C.
Now they have to select 3 distinct balls, one from each bucket and your task is to tell them that in how many ways they can choose balls.


Input:
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of the test case contains 3 integers A, B, and C.

Output:
For each test case, you have to tell the number ways they can choose balls in new line. As the number can be quite large, print them modulo 10^9+7.

Constraints:
1<=T<=10^4
1<=A,B,C<=10^18

Input:
2
4 2 2
1 1 2

Output:
4
0

"""

test=int(input())
for i in range(test):
    numbers=list(map(int,input().split()))
    numbers.sort() # 3 log3 (ignored)
    ans=1
    count=0
    for i in numbers: # 3 iterations..
        ans=(ans*(i-count))%(pow(10,9)+7)
        count+=1
    print(ans)
    
# compexity analysis:-
   # O(T*(3log3+3+constant))
   #O(T)
   #T :-Test cases..
   

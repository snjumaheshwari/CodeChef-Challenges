"""  Scube  is working on a recursion, which is same as the following function.

string f( int N ) {

if (N == 0) return "a";

if (N == 1) return "b";

if (N == 2) return "c";

return f( N - 1 ) + f( N - 2 ) + f( N - 3 );

}

But he doesn't have time to code this, so he will give you two number N and K, find the Kth character in the string returned by f(N).

Input:
    The first line contains two integers N and K.
Output:
If the string returned by f(N) has a length less than K output −1.
Otherwise, print the Kth character in the string.

Constraints
0≤N≤35
1≤K≤10**9
Sample Input:
2 1
Sample Output:
c
Sample Input:
3 2
Sample Output:
b
Sample Input:
5 8
Sample Output:
a

"""

list=["a","b","c"]
length=[1,1,1]
k=int(input())
if(k<=3):
    print(list[k-1])

else:
    k=k-3
    for i in range(35):
        list.append(list[-1]+list[-2]+list[-3])
        list.pop(0)
        x=length[-1]+length[-2]+length[-3]
        length.append(x)
        length.pop(0)
        if(x>=k ):
            print(list[-1][k-1])
            break
        else:
            k-=x
    else:
        print("-1")



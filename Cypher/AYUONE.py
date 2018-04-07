#https://www.codechef.com/CAD22018/problems/AYUONE/
"""

Ayush (ayu111) loves "1" too much and is obsessed with it.Now his friend, Shyamu introduced him a new digit "0". So he starts using it too.
He creates numbers only with these two digits and creates a list with infinite numbers. Note that the list starts with 1, because he still loves "1" more.
He asks you to guess the Nth number in the list, if it is sorted in ascending order.

Input:
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, one integer N.
Output:
For each testcase, output in a single line, a single integer which is at Nth position in the list.

Constraints
1≤T≤1000
1≤N≤105
Subtasks
30 points : 1≤T,N≤10
70 points : Original Constraints
Sample Input:
2
2
4

Sample Output:
10
100
"""

def dec_to_base(num, base=2):
    s = ""
    while (num != 0):
        rem = num % base
        num = num // base
        s = s + str(rem)
    return ('0' if s == '' else s[::-1])


test = int(input())
for i in range(test):
    n = int(input())
    print(dec_to_base(n))




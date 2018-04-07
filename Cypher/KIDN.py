#https://www.codechef.com/CAD22018/problems/KIDN
"""
All submissions for this problem are available.
CODE APOCALYPSE 3.0 is going on and Sameer and Ayush desperately wants to win this time .
They know they are not the best coders in the college. They have the ranking of first day of CODE APOCALYPSE and
they know which teams are better than them so they decided to kidnap all those teams that are better than them .
(a team is better than other team if that team have a better rank in the ranklist )
To kidnap any team the cost is the length of that team(no of characters in the name of the team ) .

You are given the Day 1 rank-list of CODE APOCALYPSE 3.0 in shuffled order.
Print the list of all the teams that will be required to kidnapped in separate lines Last line will show the cost of kidnapping the above teams.
Input
First line contains integer T, number of test cases.
First line of each test case contains a string s (name of there team) and integer n(no of teams in the last contest).
Next n lines contains a string str(name of that team ) and integer r(rank of the team) .

Output
For each test case print print the team name of all the teams(in seprate lines) who are better than there team according to there ranks .
and in the last line print the cost to kidnap the teams

Note
The list of teams that are to be kidnapped should be printed rankwise and in seprate linse
If the team has rank 1 on given ranklist simply print 0
No team name contains spaces

Constraints
1<= T<=10
1<= N<=105
Example
Input:
1
Samtech 5
humble_fools 3
glory 1
raw 2
Samtech 4
tesla 5

Output:
glory
raw
humble_fools
20
"""
test=int(input())
for i in range(test):
    cheater,n=input().split()
    n=int(n)
    list=[0]*n
    for i in range(n):
        name,rank=input().split()
        rank=int(rank)-1
        list[rank]=name
        if(name==cheater):
            ch_rank=rank
    list=list[0:ch_rank]
    count_len=0
    for i in sorted(list):
        print(i)
        count_len+=len(i)
    print(count_len)




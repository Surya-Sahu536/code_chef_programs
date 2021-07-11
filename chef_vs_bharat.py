# cook your dish here

""""Input
Chef and his friend Bharat have decided to play the game "The Chefora Spell".

In the game, a positive integer N (in decimal system) is considered a "Chefora" if the number of digits d is odd and it satisfies the equation
N=∑i=0d−1Ni⋅10i,
where Ni is the i-th digit of N from the left in 0-based indexing.

Let Ai denote the i-th smallest Chefora number.

They'll ask each other Q questions, where each question contains two integers L and R. The opponent then has to answer with

(∏i=L+1R(AL)Ai)mod109+7.
Bharat has answered all the questions right, and now it is Chef's turn. But since Chef fears that he could get some questions wrong, you have come to his rescue!
The first line contains an integer Q - the number of questions Bharat asks.
Each of the next Q lines contains two integers L and R.
Output
Print Q integers - the answers to the questions on separate lines.

Constraints
1≤Q≤105
1≤L<R≤105
Subtasks
Subtask #1 (30 points):

1≤Q≤5⋅103
1≤L<R≤5⋅103
Subtask #2 (70 points): Original constraints

Sample Input
2
1 2
9 11
Sample Output
1
541416750
Explanation
For the first question:
(A1)A2=12=1.
For the second question:
(A9)A10⋅(A9)A11=9101⋅9111≡541416750(mod109+7).

""""
def power(base,powr):
    mod = 10**9+7
    res = 1
    while powr!=0:
        if powr%2==0:
            base = ((base%mod)*(base%mod))%mod
            powr = powr//2
        else:
            res = ((res%mod)*(base%mod))%mod
            powr = powr-1
    return res

#chefora find
def chefola(num):
    paln = num
    num = num//10
    while num>0:
        paln = paln*10+num%10
        num = num//10
    return paln

arr = [0]*(10**5+1)

arradd = [0]*(10**5+1)
for i in range(1,10**5+1):
    arr[i] = chefola(i)
    arradd[i] = arradd[i-1] + arr[i]

for _ in range(int(input())):
    l,r = map(int,input().split())
    powr = arradd[r]-arradd[l]
    print(power(arr[l],powr))

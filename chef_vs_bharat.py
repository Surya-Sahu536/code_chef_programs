# cook your dish here
#
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

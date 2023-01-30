
import sys

T=int(input())

for i in range(1,T+1):
    a,b=map(int,input().split())
    ans1=a//b
    ans2=a%b
    print(f'#{i} {ans1} {ans2}' )



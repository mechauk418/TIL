T=int(input())

for i in range(T):
    N=int(input())
    ans1=0
    ans2=0

    for j in range(1,N+1):
        if j % 2 ==1:
            ans1+=j
        else:
            ans2-=j
        
        ans = ans1+ans2

    
    print( f'#{i+1} {ans}' )
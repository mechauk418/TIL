
T=int(input())

for i in range(T):
    P,Q,R,S,W=map(int,input().split())
    
    ans1 = P * W
    if W<=R:
        ans2 = Q
    else:
        ans2 = Q+ (W-R)*S

    if ans1 >= ans2:
        print( f'#{i+1} {ans2}' )
    else:
        print( f'#{i+1} {ans1}' )
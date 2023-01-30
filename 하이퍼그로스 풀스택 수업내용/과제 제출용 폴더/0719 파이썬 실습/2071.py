T=int(input())

for i in range(1,T+1):
    n_list=list(map(int,input().split()))
    ans1=sum(n_list)/len(n_list)
    ans1 = int(round(ans1,0))
    print(f'#{i} {ans1}' )
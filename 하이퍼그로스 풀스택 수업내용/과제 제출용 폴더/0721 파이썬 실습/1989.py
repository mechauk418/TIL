
T=int(input())

for i in range(1,T+1):
    S=input()
    S_reverse = S[::-1]

    if S == S_reverse:
        print(f'#{i} {1}')
    else:
        print(f'#{i} {0}')


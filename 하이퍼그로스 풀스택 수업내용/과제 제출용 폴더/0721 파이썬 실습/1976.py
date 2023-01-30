
T=int(input())

for i in range(1,T+1):
    H1,M1,H2,M2 = map(int,input().split())

    if M1 + M2 >= 60:
        H3 = H1 + H2 + 1
        M3 = M1 + M2 - 60
        if H3>12:
            H3=H3-12

    else:
        H3 = H1 + H2
        if H3>12:
            H3=H3-12
        M3 = M1 + M2

    print(f'#{i} {H3} {M3}')

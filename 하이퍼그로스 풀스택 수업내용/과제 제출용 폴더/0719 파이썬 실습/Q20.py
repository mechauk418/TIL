
import math as m



try:
    N=int(input())

    cnt = int(m.log10(N))
    ans = 0
    while True:
        S = N % 10
        N = N // 10
        ans += S * 10**cnt
        cnt += -1

        if N==0:
            break

    print(ans)

except ValueError:
    print(0)

N=int(input())


Ans = [ 1 * 2** i for i in range(N+1)  ]

print( ' '.join(map(str,Ans)))
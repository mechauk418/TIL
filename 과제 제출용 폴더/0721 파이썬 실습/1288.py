
T=int(input())

for i in range(T):

    N=int(input())
    k=1
    N_list=[]
    num_list=[str(i) for i in range(10)]
    while True:
        N_list.append(str(k*N))
        ans = ''.join(N_list)

        if all(word in ans for word in num_list):
            break

        k+=1

    print(f'#{i+1} {k*N}')




N=int(input())

N_list = [ str(i) for i in range(1,N+1) ]

def threesixnine(n):
    cnt = n.count('3') + n.count('6') + n.count('9')
    if cnt == 0:
        return n
    else:
        return '-' * cnt

ans = list(map(threesixnine,N_list))
print(' '.join(ans))
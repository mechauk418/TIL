N=int(input())

N_list = [ str(i) for i in range(1,N+1) ]
R_list3 = ['0']*N



for i in range(N):
    if '3' in N_list[i] and ( '0' in N_list[i] or '1' in N_list[i] or '2' in N_list[i] or '4' in N_list[i] or '5' in N_list[i] or '7' in N_list[i] or '8' in N_list[i]):
        R_list3[i] = '-'
    elif '3' in N_list[i]:
        R_list3[i] = N_list[i].replace('3','-')
    else:
        R_list3[i] = N_list[i]

N_list = R_list3

for i in range(N):
    if '6' in N_list[i] and ( '0' in N_list[i] or '1' in N_list[i] or '2' in N_list[i] or '4' in N_list[i] or '5' in N_list[i] or '7' in N_list[i] or '8' in N_list[i]):
        R_list3[i] = '-'
    elif '6' in N_list[i]:
        R_list3[i] = N_list[i].replace('6','-')
    else:
        R_list3[i] = N_list[i]

N_list = R_list3

for i in range(N):
    if '9' in N_list[i] and ( '0' in N_list[i] or '1' in N_list[i] or '2' in N_list[i] or '4' in N_list[i] or '5' in N_list[i] or '7' in N_list[i] or '8' in N_list[i]):
        R_list3[i] = '-'
    elif '9' in N_list[i]:
        R_list3[i] = N_list[i].replace('9','-')
    else:
        R_list3[i] = N_list[i]

N_list = R_list3

print( ' '.join(N_list)   )
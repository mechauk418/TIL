N=int(input())

if 0<=N<30:
    print('좋음')

elif 30<=N<80:
    print('보통')
elif 80<=N<150:
    print('나쁨')

else:
    print('매우 나쁨')
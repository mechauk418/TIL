# CodeUp 파이썬 기초 100제





## 6001번 기초 출력

```python
print( )를 이용해 다음 단어를 출력하시오.
Hello

#ans
print("Hello")
```



## 6002번 기초 출력

```python
이번에는 공백( )을 포함한 문장을 출력한다.
다음 문장을 출력해보자.
Hello World

#ans
print("Hello World")
```



## 6003번 기초 출력

```python
이번에는 줄을 바꿔 출력하는 출력문을 연습해보자.
다음과 같이 줄을 바꿔 출력해야 한다.
Hello
World

#ans
print("Hello\nWorld")
```



## 6004번 기초 출력

```python
다음 문장을 출력하시오.
'Hello'

#ans
print("'Hello'")
```



## 6005번 기초 출력

```python
다음 문장을 출력하시오.
"Hello"

#ans
print('"Hello"')
```



## 6006번 기초 출력

```python
다음 문장을 출력하시오.
"!@#$%^&*()'
(단, 큰따옴표와 작은따옴표도 함께 출력한다.)

#ans
print("\"!@#$%^&*()\'")
```



## 6007번 기초 출력

```python
파일 경로에는 특수문자들이 포함된다.
다음 경로를 출력하시오.
"C:\Download\'hello'.py"
(단, 따옴표도 함께 출력한다.)

#ans
print('''"C:\Download\\'hello'.py"''')
```



## 6008번 기초 출력

```python
이번에는 다음과 같은 python프로그램의 소스코드를 출력해보자.
print("Hello\nWorld")
위 코드를 정확히 그대로 출력하시오.(공백문자 주의)

#ans
print('''print("Hello\\nWorld")''')
```



## 6009번 기초 입출력

```python
변수에 문자 1개를 저장한 후
변수에 저장되어 있는 문자를 그대로 출력해보자.

#ans
c=input()
print(c)
```



## 6010번 기초 입출력

```python
변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.

#ans
n=input()
n=int(n)
print(n)
```



## 6011번 기초 입출력

```python
변수에 실수값을 저장한 후 실수로 변환하여 출력해보자.

#ans
n=input()
n=float(n)
print(n)
```



## 6012번 기초 입출력

```python
줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

#ans
a = input() 
b = input()
a=int(a)
b=int(b)
print(a)
print(b)

```



## 6013번 기초 입출력

```python
줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.

#ans
A=input()
B=input()

print(B)
print(A)
```



## 6014번 기초 입출력

```python
실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

#ans
A=input()
print(A)
print(A)
print(A)
```



## 6015번 기초 입출력

```python
공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

#ans
n,m=map(int,input().split())
print(n)
print(m)
```



## 6016번 기초 입출력

```python
공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

#ans
n,m=map(str,input().split())
print(m)
print(n)
```



## 6017번 기초 입출력

```python
정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

#ans
s = input()
print(s, s, s) 
```



## 6018번 기초 입출력

```python
24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

#ans
a, b = input().split(':')
print(a, b, sep=':')
```



## 6019번 기초 입출력

```python
"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

#ans
a, b,c = input().split('.')
print(c, b, a, sep='-')
```



## 6020번 기초 입출력

```python
주민번호는 다음과 같이 구성된다.
XXXXXX-XXXXXXX

왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
주민번호를 입력받아 형태를 바꿔 출력해보자.

#ans
a,b=input().split('-')
print(a+b)
```



## 6021번 기초 입출력

```python
알파벳과 숫자로 이루어진 단어 1개가 입력된다.
입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

예시
s = input()
print(s[0])
print(s[1])

#ans
s=input()
for i in range(len(s)):
    print(s[i])
```



## 6022번 기초 입출력

```python
6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

참고
s = input()
print(s[0:2])

#ans
s=input()
print(s[0:2],s[2:4],s[4:6])
```



## 6023번 기초 입출력

```python
시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.
        
#ans
a,b,c=input().split(':')
print(b)
```



## 6024번 기초 입출력

```python
알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
순서대로 붙여 출력하는 프로그램을 작성해보자.

#ans
w1, w2 = input().split()
s = w1 + w2
print(s)
```



## 6025번 기초 값변환

```python
정수 2개를 입력받아
합을 출력하는 프로그램을 작성해보자.

#ans
n,m=input().split()
c=int(n)+int(m)
print(c)
```



## 6026번 기초 값변환

```python
실수 2개를 입력받아
합을 출력하는 프로그램을 작성해보자.

#ans
n,m=input().split()
c=float(n)+float(m)
print(c)
```



## 6032

```python
입력된 정수의 부호를 바꿔 출력해보자.

#ans
n=int(input())
print(-n)
```



## 6033번 기초 산술연산

```python
문자 1개를 입력받아 그 다음 문자를 출력해보자.
영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

#ans
n=input()
b=int(ord(n))+1
print(chr(b))
```



## 6034번 기초 산술연산

```python
정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

n,m=map(int,input().split())
print(n-m)
```



## 6035번 기초 산술연산

```python
실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

#ans
n,m=map(float,input().split())
print(n*m)
```



## 6036번 기초 산술연산

```python
단어와 반복 횟수를 입력받아 여러 번 출력해보자.

#ans
w, n = input().split()
print(w*int(n))
```



## 6037번 기초 산술연산

```python
반복 횟수와 문장을 입력받아 여러 번 출력해보자.

#ans
n = input()
s = input()
print(int(n)*s)
```



## 6038번 기초 산술연산

```python
정수 2개(a, b)를 입력받아
a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.

#ans
a,b=map(int,input().split())
print(a**b)
```



## 6039번 기초 산술연산

```python
실수 2개(f1, f2)를 입력받아
f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

#ans
f1,f2=map(float,input().split())
print((f1)**(f2))
```



## 6040번 기초 산술연산

```python
정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

#ans
a,b=map(int,input().split())
print(a//b)
```



## 6041번 기초 산술연산

```python
정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.

#ans
a,b=map(int,input().split())
print(a%b)
```



## 6042번 기초 값변환

```python
실수 1개를 입력받아
소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.

#ans
a=input()
a=float(a)
print( format(a, ".2f") )
```



## 6043번 기초 산술연산

```python
실수 2개(f1, f2)를 입력받아
f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

#ans
f1,f2 =map(float,input().split())
s=f1/f2
print(format(s,".3f"))
```



## 6044번 기초 산술연산

```python
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단, b는 0이 아니다.

#ans
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f"))

```



## 6045번 기초 산술연산

```python
정수 3개를 입력받아 합과 평균을 출력해보자.

#ans
a,b,c=map(int,input().split())
print(a+b+c, end=' ')
d=a+b+c
print(format(d/3, ".2f"))
```



## 6046번 기초 비트시프트연산

```python
정수 1개를 입력받아 2배 곱해 출력해보자.

참고
*2 를 계산한 값을 출력해도 되지만,
정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용할 수 있다.
컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,
2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
가장 오른쪽에 있는 1비트는 사라진다.

예시
n = 10
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

#ans
n=int(input())
print(n<<1)
```



## 6047번 기초 비트시프트연산

```python
정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
0 <= a <= 10, 0 <= b <= 10

#ans
a,b=map(int,(input().split()))
print(a<<b)
```



## 6048번 기초 비교연산

```python
두 정수(a, b)를 입력받아
a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

#ans
a,b=map(int,(input().split()))

if a<b:
    print(True)

else:
    print(False)
```



## 6049번 기초 비교연산

```python
두 정수(a, b)를 입력받아
a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

#ans
a,b=map(int,(input().split()))

if a==b:
    print(True)

else:
    print(False)

```



## 6050번 기초 비교연산

```python
두 정수(a, b)를 입력받아
b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

#ans
a,b=map(int,(input().split()))

if b>=a:
    print(True)
else:
    print(False)
```



## 6051번 기초 비교연산

```python
두 정수(a, b)를 입력받아
a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.

#ans
a,b=map(int,(input().split()))
if a!=b:
    print(True)
else:
    print(False)
```



## 6052번 기초 논리연산

```python
정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.

#ans
n=int(input())
print(bool(n))
```



## 6053번 기초 논리연산

```python
정수값이 입력될 때,
그 불 값을 반대로 출력하는 프로그램을 작성해보자.

#ans
n=int(input())
print(not bool(n))
```



## 6054번 기초 논리연산

```python
2개의 정수값이 입력될 때,
그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

#ans
a, b = input().split()
print(bool(int(a)) and bool(int(b)))
```



## 6055번 기초 논리연산

```python
2개의 정수값이 입력될 때,
그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

#ans
a, b = input().split()
print(bool(int(a)) or bool(int(b)))
```



## 6056번 기초 논리연산

```python
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

#ans
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

```



## 6057번 기초 논리연산

```python
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

#ans
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and d) or ((not c) and (not d)))
```



## 6058번 기초 논리연산

```python
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.

#ans
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((not c) and (not d))
```

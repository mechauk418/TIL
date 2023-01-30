# CodeUp 파이썬 기초 100제 - 2





## 6063번 기초 3항연산

```python
입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.


#ans
a,b=map(int,input().split())
c=(a if (a>=b) else b)
print(c)
```



## 6064번 기초 3항연산

```python
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.

#ans
a,b,c=map(int,input().split())
d=(a if (a<=(b if (b<=c) else c)) else (b if (b<=c) else c))
print(d)
```



## 6065번 기초 조건/선택 실행구조

```python
3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.


#ans
a,b,c=map(int,input().split())

if a%2==0:
    print(a)

if b%2==0:
    print(b)

if c%2==0:
    print(c)
```



## 6066번 기초 조건/선택 실행구조

```python
3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

#ans
a,b,c=map(int,input().split())

if a%2==0:
    print("even")

else:
    print("odd")

if b % 2 == 0:
    print("even")

else:
    print("odd")

if c % 2 == 0:
    print("even")

else:
    print("odd")
```



## 6067번 기초 출력

```python
0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
음수이면서 짝수이면, A
음수이면서 홀수이면, B
양수이면서 짝수이면, C
양수이면서 홀수이면, D
를 출력한다.


#ans
n=int(input())
if n<0 :
  if n%2==0 :
    print('A')      
  else :
    print('B')
else :
  if n%2==0 :
    print('C')
  else :
    print('D')

```



## 6068번 기초 출력

```python
점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

평가 기준
점수 범위 : 평가
 90 ~ 100 : A
 70 ~   89 : B
 40 ~   69 : C
   0 ~   39 : D
로 평가되어야 한다.

#ans
n=int(input())

if n>=90:
    print('A')

elif 89>=n>=70:
    print('B')

elif 69>=n>=40:
    print('C')

else:
    print('D')
```



## 6069번 기초 출력

```python
다음 문장을 출력하시오.
"!@#$%^&*()'
(단, 큰따옴표와 작은따옴표도 함께 출력한다.)

#ans
print("\"!@#$%^&*()\'")
```



## 6070번 기초 출력

```python
파일 경로에는 특수문자들이 포함된다.
다음 경로를 출력하시오.
"C:\Download\'hello'.py"
(단, 따옴표도 함께 출력한다.)

#ans
print('''"C:\Download\\'hello'.py"''')
```



## 6071번 기초 출력

```python
이번에는 다음과 같은 python프로그램의 소스코드를 출력해보자.
print("Hello\nWorld")
위 코드를 정확히 그대로 출력하시오.(공백문자 주의)

#ans
print('''print("Hello\\nWorld")''')
```



## 6072번 기초 입출력

```python
변수에 문자 1개를 저장한 후
변수에 저장되어 있는 문자를 그대로 출력해보자.

#ans
c=input()
print(c)
```



## 6073번 기초 입출력

```python
변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.

#ans
n=input()
n=int(n)
print(n)
```



## 6074번 기초 입출력

```python
변수에 실수값을 저장한 후 실수로 변환하여 출력해보자.

#ans
n=input()
n=float(n)
print(n)
```



## 6075번 기초 입출력

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



## 6076번 기초 입출력

```python
줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.

#ans
A=input()
B=input()

print(B)
print(A)
```



## 6077번 기초 입출력

```python
실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

#ans
A=input()
print(A)
print(A)
print(A)
```



## 6078번 기초 입출력

```python
공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

#ans
n,m=map(int,input().split())
print(n)
print(m)
```



## 6079번 기초 입출력

```python
공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

#ans
n,m=map(str,input().split())
print(m)
print(n)
```



## 6080번 기초 입출력

```python
정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

#ans
s = input()
print(s, s, s) 
```



## 6081번 기초 입출력

```python
24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

#ans
a, b = input().split(':')
print(a, b, sep=':')
```



## 6082번 기초 입출력

```python
"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

#ans
a, b,c = input().split('.')
print(c, b, a, sep='-')
```



## 6083번 기초 입출력

```python
주민번호는 다음과 같이 구성된다.
XXXXXX-XXXXXXX

왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
주민번호를 입력받아 형태를 바꿔 출력해보자.

#ans
a,b=input().split('-')
print(a+b)
```



## 6084번 기초 입출력

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



## 6085번 기초 입출력

```python
6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

참고
s = input()
print(s[0:2])

#ans
s=input()
print(s[0:2],s[2:4],s[4:6])
```



## 6086번 기초 입출력

```python
시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.
        
#ans
a,b,c=input().split(':')
print(b)
```



## 6087번 기초 입출력

```python
알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
순서대로 붙여 출력하는 프로그램을 작성해보자.

#ans
w1, w2 = input().split()
s = w1 + w2
print(s)
```



## 6088번 기초 값변환

```python
정수 2개를 입력받아
합을 출력하는 프로그램을 작성해보자.

#ans
n,m=input().split()
c=int(n)+int(m)
print(c)
```



## 6089번 기초 값변환

```python
실수 2개를 입력받아
합을 출력하는 프로그램을 작성해보자.

#ans
n,m=input().split()
c=float(n)+float(m)
print(c)
```



## 6090

```python
입력된 정수의 부호를 바꿔 출력해보자.

#ans
n=int(input())
print(-n)
```



## 6091번 기초 산술연산

```python
문자 1개를 입력받아 그 다음 문자를 출력해보자.
영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

#ans
n=input()
b=int(ord(n))+1
print(chr(b))
```



## 6092번 기초 산술연산

```python
정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

n,m=map(int,input().split())
print(n-m)
```



## 6093번 기초 산술연산

```python
실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

#ans
n,m=map(float,input().split())
print(n*m)
```



## 6094번 기초 산술연산

```python
단어와 반복 횟수를 입력받아 여러 번 출력해보자.

#ans
w, n = input().split()
print(w*int(n))
```


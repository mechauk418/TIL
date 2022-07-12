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


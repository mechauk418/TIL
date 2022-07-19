# bin()



`bin()` 은 정수를 앞에 `0b` 를 붙인 2진수로 변환하여 반환하는 함수이다.

```python
x = bin(5)
print(x) # 0b101
```

여기서 `0b`가 붙는 이유는 파이썬은 10진수를 사용하기 때문에 2진수, 8진수, 16진수를 표현할때는 숫자 앞에 접두어로 특정 문자를 붙여줘야한다.

`0b` : 2진수 접두어 (***bin**ary의 b)

`0o` : 8진수 접두어 (**oct**al의 o)

`0x` : 16진수의 접두어 (**hex**adecimal 의 x)

각 진수의 영어표기를 보면 8진수, 16진수를 변환해주는 함수도 알 수 있다.



# oct()

정수를 8진수로 변환하여 반환하는 함수이다.

```python
x = oct(5)
print(x) # 0o5
```



# hex()

정수를 16진수로 변환하여 반환하는 함수이다.

```python
x = hex(5)
print(x) # 0x5
```



---



중요한 것은 `bin(), oct(), hex()` 함수의 타입이다.

```python
a=bin(5)
b=oct(5)
c=hex(5)

print(type(a),type(b),type(c)) # str, str, str
```

위의 코드를 보면 세 함수의 반환값이 문자열인 것을 알 수 있다.

이를 다시 10진수로 변환하기 위해서는 `int()` 함수를 사용할 수 있다.

`int()` 함수는 흔히 정수로 변환하는 함수로 알고있지만 아래와 같이 사용하면 문자열을 10진수 숫자로 변환하여 반환하는 기능이 있다.

```python
a=bin(5)
print(a) # 0b101

d=int(a,2) # d= int('0b101',2 ) 와 같다.
print(d) # 5
```



## 참고

[파이썬 자습서](https://docs.python.org/ko/3/library/functions.html#bin)

[점프투파이썬](https://wikidocs.net/32#int)
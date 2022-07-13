# abs(x)



x의 절대값을 '반환'하는 함수이다.

또한 반환된 값은 입력된 값과 같은 타입이다.

```python
x=-5
abs(x)
print(x) # -5
print(abs(x)) # 5
print(type(abs(x))) # int
```



복소수에서의 절대값은 조금 다르게 계산된다.

x=a+bj라는 복소수의 절대값은 아래와 같다.
$$
abs(x) =\sqrt(a^2 + b^2)
$$

```python
x=3+4j
print(abs(x)) # 5
```


# all()

`all()` 함수는 인자의 객체의 요소가 모두 참일 경우 `True`를 반환하는 내장 함수이다. 다시 말해 하나라도 거짓일 경우 `False` 를 반환한다. 

`all()` 함수는 반복 가능한 객체(iterable)를 인자로 받을 수 있다.

예제는 다음과 같다.

```python
test=all([1,2,3,4,5])
print(test) # True

test=all([1,2,3,4,0])
print(test) # False

test=all([1,2,3,4,3>5])  # 3>5 라는 조건문이 요소로 들어가있음.
print(test) # False

print(all([])) # True / all() 함수은 빈칸에 대해서 True를 반환한다.
```



제너레이터 컴프리헨션과 조합하면 다음처럼 활용할 수 있다.

```python
test = all(num > 0 and num % 2 == 0 for num in [2, 4, 6, 8])
print(test) # True
```





# any()

`any()` 함수는 `all()` 함수와 반대의 기능을 한다.

객체의 요소가 하나라도 참일 경우 `True`를 반환하고, 모두 거짓일 경우에만 `False`를 반환하는 함수이다.

```python
test=any([1,2,3,4,5])
print(test) # True

test=any([1,0,0,0,0])
print(test) # True

test=any([1>9, 2>6 ,3>5])
print(test) # False

print(any([])) # False / any() 함수은 빈칸에 대해서 False를 반환한다.
```





## 참고



[DaleSeo](https://www.daleseo.com/python-all/) 


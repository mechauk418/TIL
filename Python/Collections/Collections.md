# Collections



파이썬에서 자주 사용하는 `collections` 모듈을 정리한다.



## 1. Counter



`counter`는 문자열이나 리스트에서 요소의 갯수를 딕셔너리로 반환하는 클래스이다



```python
import collections

S=[A,A,A,B,B,C,C,C] # 리스트
dict1={}
dict1=collections.Counter(S_list)
print(dict1) # {'A': 3, 'B': 2, 'C': 3} 
```

```python
import collections

S='AAABBCCC' # 문자열
A=collections.Counter(S)

print(A) # Counter({'A': 3, 'C': 3, 'B': 2})
print(type(A)) # <class 'collections.Counter'>

print(A.keys()) # dict_keys(['A', 'B', 'C'])
print(A['A']) # 3
```



`counter`으로 반환된 객체는 딕셔너리처럼 사용 가능하다.
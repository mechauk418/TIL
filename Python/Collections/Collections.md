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



## 2. defaultdict



`defaultdict` 는 딕셔너리를 만드는 서브클래스이다.



딕셔너리의 기본값 타입을 미리 지정할 수 있다. (int, list, set 등등)



기본값을 list로 지정한 예시



```python
from collections import defaultdict

listdict = defaultdict(list)
listdict['first']
listdict['second'] = 'sec'
listdict['third'].append('third')

print(listdict)

defaultdict(<class 'list'>, {'first': [], 'second': 'sec', 'third': ['third']})

```



`defaultdict` 가 유용한 이유는 예를 들어서 리스트 내부의 알파벳의 갯수를 센다고 할때 딕셔너리로 A: 갯수, B:갯수 처럼 표현한다고 하자.



그런데 맨 처음 딕셔너리에 A나 B가 없으므로 키 값의 존재 유무를 판단하고 밸류의 값을 변경해주어야 하는데 `defaultdict` 를 int로 지정하면 자동으로 0으로 초기화해주기 때문에 편하다.
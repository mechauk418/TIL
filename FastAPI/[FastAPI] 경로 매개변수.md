# [FastAPI] 경로 매개변수



### 변수 타입 선언

```python
from fastapi import FastAPI

app = FastAPI()

# 매개변수 타입 미지정
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
    
# 매개변수에 int 타입 선언
@app.get("/items/{item_id}")    
async def read_item(item_id: int):
    return {"item_id": item_id}

```

파이썬 함수 문법처럼 매개변수에 직접 타입 선언이 가능하다.


### 경로 순서 문제

유저 닉네임으로 유저 정보를 조회하는 API가 있다고 해보자.

`users/{user_nickname}` 의 경로를 가지고, 당연히 `user_nickname`는 `str` 타입이다.

그런데 내 정보만 보기 위해 `users/me` 라는 경로의 API를 추가한다면? 

`me`라는 닉네임의 유저 정보를 출력해야할지 나의 정보를 출력해야할지 문제가 생긴다.

이러한 상황을 해결하기 위해서는 우선 순위의 함수를 먼저 선언해주면 된다.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_nickname}")
async def read_user(user_nickname: str):
    return {"user_nickname": user_nickname}

```

### 매개변수 범위 지정 (Enum 클래스)

매개변수로 들어오는 값을 정하고싶다면 `Enum` 클래스를 활용한다.

```python

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class ModelName(str,Enum):
    first = "first"
    second = "second"
    third = "third"


@app.get("/users/{user_id}")
async def read_user(user_id: ModelName):
    if user_id is ModelName.first:
        return {"choice":user_id, "message":"first"}
    elif user_id.value == "second":
        return {"choice":user_id, "message":"second"}
    elif user_id is ModelName.third:
        return {"choice":user_id, "message":"third"}

```

매개변수를 `Enum` 로 생성한 클래스를 넣어야한다.
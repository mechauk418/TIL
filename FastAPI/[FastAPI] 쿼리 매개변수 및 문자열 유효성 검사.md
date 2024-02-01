# [FastAPI] 쿼리 매개변수 및 문자열 유효성 검사



### 기본 유효성 검사

```python

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

```

`Union` 을 통해 유효성검사를 할 수 있다.

### 추가 검증

위에서 매개변수로 받은 q에 대해 추가적인 검증을 할 수 있다.

`typing` 패키지의 `Annotated` 클래스를 사용한다.
(3.9 이하에선 `typing_extensions` 패키지에서 가져온다.)

`Annotated` 클래스는 자세한 내용을 찾기 힘들었지만 간단하게 요약하면 매개변수에 메타데이터를 추가하는 모듈이다.

```
Annotated[int, ValueRange(-10, 5)]
```
이런 형태로 사용되며, 첫번째로 오는 `int` 이 실제 데이터의 형태, 뒤에 오는 매개변수들이 메타데이터가 된다.

즉, 매개변수에 추가적인 검증을 할 수 있는 것이다.

```python

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

```

### 결론

```python
from typing import Annotated, Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

```

결론적으로 위와 같이 `Query` 클래스와 `Annotated` 클래스 사용하여 여러개의 메타데이터를 설정할 수 있다.
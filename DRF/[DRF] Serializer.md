

# Serializer 



### Serializer란?



`Serializer` 는 Django 모델 인스턴스나 쿼리셋을 JSON 형식으로 변환하는 역할을 한다.

이 과정을 직렬화라고 부른다.

반대로 JSON을 Django 모델 인스턴스나 쿼리셋으로 변환하는 작업은 역직렬화라고 부른다.



### Serializer 작성하기



```python
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'content']
```



`Serializer ` 를 작성하기 위해서는 `Serializers` 클래스에서 `ModelSerializer `를 상속받아서 작성해준다.

`Meta` 클래스에는 `Serializer ` 의 속성이 담긴다.



```
1. model : 직렬화할 모델 클래스를 지정한다.

2. fields : 직렬화할 필드를 정의한다.

3. exclude : 직렬화에서 제외할 필드를 지정한다. (fields와 exclude는 하나만 사용할 수 있다.)

4. read_only_fields : 읽기 전용 필드를 정의한다.

5. extra_kwargs : 특정 필드에 대한 추가적인 설정을 할 수 있다. (사용자 정의 검증, 권한 등등)

6. validators : 유효성 검사 검즈익를 설정한다.
```



### 중첩된 시리얼라이저 (Nested Serializer)



```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'nationality']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'price']
```


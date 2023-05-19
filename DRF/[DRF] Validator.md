

# Validator





DRF에서 유효성 검사를 하는 방법은 두가지가 있다.



model에서 유효성 검사를 하는 것과 serializer에서 유효성 검사를 하는 것이다.



가급적이면 model에서 유효성 검사를 선언하는 것이 좋다





## model



model에서 유효성 검사는 두가지 방법으로 이루어진다.



1. Field에서 옵션 인자로 지정하기
2. Validator을 커스텀하여 구현하기



### 1. Field 옵션 추가하기



django에서 기본으로 제공하는 validator 함수를 필드에 인자로 주어 유효성 검사를 하는 방법이다.



- RegexValidator
- EmailValidator
- URLValidator
- MaxValueValidator



등등 이외에도 다양한 기본으로 제공하는 Validator 함수가 있다.

다른 함수는 [Django Validator 공식 문서](https://docs.djangoproject.com/en/3.2/ref/validators/) 에서 볼 수 있다.





### 2. Validator 커스텀하여 구현하기



원하는 Validator이 없다면 직접 커스텀하여 구현할 수 있다.



```python
# validators.py
from django.core.exceptions import ValidationError

def validate_test(value):
    if 'k' in value:
        raise ValidationError('유효성 검사 실패')
        
        
# models.py

from .validators import *

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    create_user = models.CharField(max_length=80)
    team = models.CharField(max_length=80, choices=team_list)
    title = models.CharField(max_length=80, validators=[validate_test])
```



`validators.py` 에서 유효성 함수를 작성해준뒤 `models.py`에서 호출하여 사용한다.





## serializer 



`serializer`에서 유효성 검사를 하는 방법은 두가지가 있다.

- Field 단일 유효성 검사
- object 유효성 검사



### Field validator



단일 필드를 검사하는 것이다.



```python
# serializers.py

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class TaskSerializer(serializers.ModelSerializer):
    team = serializers.ChoiceField(choices = team_list, style={'base_template' : 'radio.html'})
    test = serializers.SerializerMethodField()
    subchoic = serializers.MultipleChoiceField(choices = team_list, write_only=True)


    def validate_title(self,value):
        if len(value) < 20:
            raise serializers.ValidationError('title error')
```



`serializer` 내부에서 `validate_{field name}` 로 단일 필드에 대한 유효성 함수를 작성하는 방식이다.



### object validator



```python
# serializers.py

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class TaskSerializer(serializers.ModelSerializer):
    team = serializers.ChoiceField(choices = team_list, style={'base_template' : 'radio.html'})
    test = serializers.SerializerMethodField()
    subchoic = serializers.MultipleChoiceField(choices = team_list, write_only=True)
    

    def validate(self, attrs):
        if 'error' not in attrs['title']:
            raise ValidationError('error')
        return super().validate(attrs)
```



`validate` 함수에서 인자를 받고, 인자에서 필드를 꺼내서 `object` 전체에 대한 유효성 검사를 할 수 있다.


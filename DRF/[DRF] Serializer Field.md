# Serializer Field 





- `read_only` : API 출력에는 포함되지만, 객체 생성 또는 입력에는 포함되지 않는 필드 (기본값 False)

- `write_only` : 객체 생성 또는 입력에는 포함되지만 API 출력에는 사용되지 않는 필드 (기본값 False)

- `required` : 필드가 비어있어도 오류가 발생하지 않는다. 

  기본값은 `True`인데, `Model Serializer` 을 사용하는 경우 `models.py `에서 `null=True, blank = True` 로 지정할 경우 기본값이 `False`로 변한다.

- `allow_null` : `None`가 값으로 올 수 있다.

- `source` : 모델에서 특정 필드를 가져올 수 있다.

  ```python
  class LikeSerializer(serializers.ModelSerializer):
  
      user = serializers.ReadOnlyField(source="user.email")
      article = serializers.ReadOnlyField(source="article.pk")
  ```

- `validators` : 입력에 적용될 validator function 리스트

- `label` : HTML 필드 입력에서 필드 이름을 설정

- `help_text` : HTML 필드 입력에서 필드 입력창 아래 텍스트를 설정

- `initial` : HTML 필드 입력에서 입력창을 미리 특정 값으로 채워두게 설정

- `style` : 렌더러가 필드를 렌더링하는 방법을 설정함.

  ```python
  # password를 입력할때 password 타입으로 입력하게 설정
  password = serializers.CharField(
      style={'input_type': 'password'}
  )
  
  # Choice필드를 입력할때 radio form으로 입력하게 설정한다.
  color_channel = serializers.ChoiceField(
      choices=['red', 'green', 'blue'],
      style={'base_template': 'radio.html'}
  )
  ```

  
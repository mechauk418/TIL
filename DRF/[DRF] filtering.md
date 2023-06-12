# Filtering



필터링은 쿼리에서 반환되는 항목을 조건부로 제한하는 것을 말한다.



### GenericAPIView 필터링



가장 간단한 필터링은 `GenericAPIView` 에서 `.get_queryset()`를 오버라이딩하여 직접 필터링 하는 것이다.



```python
class Task_ViewSet(ModelViewSet):
    
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    # throttle_classes = [TestThrottle]
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['compleated_date', 'team',]

    def get_queryset(self):
        return super().get_queryset().filter(team='다래')
```



목록에서 팀명이 다래인 자료만 보고 싶다면 위처럼 직접 필터링하여 작성할 수 있다.



### 일반 필터링



쿼리를 재정의하는 것이 아닌 DRF에서 지원해주는 필터링 기능이다.



- 패키지 설치

  ```bash
  pip install django-filter
  ```

  <br>

  <br>

  ```python
  INSTALLED_APPS = [
      ...
      'django_filters',
      ...
  ]
  ```

  <br>

  <br>

  

- 필터 백엔드 설정

  <br>

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
  }
  ```

  <br>

  `settings.py` 에서 전역에 대한 필터 백엔드를 설정할 수 있다.

  <br>

  ```python
  class Task_ViewSet(ModelViewSet):
      
      queryset = Task.objects.all().order_by('-id')
      serializer_class = TaskSerializer
      # throttle_classes = [TestThrottle]
      filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
  ```

  <br>

  `views.py` 에서 개별 필터 백엔드를 설정하는 것도 가능하다.

  <br>

- 필터링 필드 설정

  ```python
  class Task_ViewSet(ModelViewSet):
      
      queryset = Task.objects.all().order_by('-id')
      serializer_class = TaskSerializer
      # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
      filterset_fields = ['compleated_date', 'team',]
  ```




![](https://velog.velcdn.com/images/mechauk418/post/221cbc84-a287-40c9-b2fc-36d239ffedaf/image.jpg)



![](https://velog.velcdn.com/images/mechauk418/post/2de88660-a6a0-4eef-b1b6-954b037eba83/image.jpg)



### 검색 필터



특정 필드를 검색하여 조건에 맞는 결과를 필터링한다.



간단한 단일 쿼리 매개변수 기반 검색을 지원하며, Django admin 검색 기능을 기반으로 한다.



- 일반 필드 설정

  ```python
  from rest_framework import filters
  
  class Task_ViewSet(ModelViewSet):
      
      queryset = Task.objects.all().order_by('-id')
      serializer_class = TaskSerializer
      # throttle_classes = [TestThrottle]
      filter_backends = [filters.SearchFilter]
      search_fields  = ['title','content']
  ```

  <br>

  일반적으로 `SearchFilter` 클래스를 이용한다.

  `search_fields` 에는 검색할 필드를 입력하는데 `TextField` 유형의 필드만 포함되어야 한다. (`Charfield 포함`)

  <br>

  또한, 이중 밑줄 표기법을 사용하여 중첩된 JSON 구조에서도 필터링 할 수 있다.

  ```python
  class Task_ViewSet(ModelViewSet):
      
      queryset = Task.objects.all().order_by('-id')
      serializer_class = TaskSerializer
      # throttle_classes = [TestThrottle]
      filter_backends = [filters.SearchFilter]
      search_fields  = ['title','content','subtasks__team']
  ```

  



### 순서 필터



결과를 순서대로 정렬하여 반환한다.



- 일반 필드 설정

  ```python
  from rest_framework import filters
  
  class Task_ViewSet(ModelViewSet):
      
      queryset = Task.objects.all()
      serializer_class = TaskSerializer
      # throttle_classes = [TestThrottle]
      filter_backends = [filters.OrderingFilter]
      ordering_fields = ['title','content']
      ordering  = ['title'] # ordering 기본 필드 설정
  ```

  `OrderingFilter` 클래스를 이용한다.

  `ordering_fields` 에는 정렬할 필드를 입력하고, `ordering`에는 기본 순서로 사용할 필드를 입력한다.



### 커스텀 필터링



```python
class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)
```



`BaseFilterBackend` 클래스를 상속받아 새로운 클래스를 커스텀하여 필터링백엔드를 작성할 수 있다.



### 타사 패키지



- `django-rest-framework-filters package `
- `djangorestframework-word-filter`
- `django-url-filter`
- `drf-url-filter`

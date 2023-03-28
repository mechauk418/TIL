# [DRF] format_suffix_patterns



https://www.django-rest-framework.org/api-guide/format-suffixes/#format_suffix_patterns

```python
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('', views.apt_root),
    path('comments/', views.comment_list),
    path('comments/<int:pk>/', views.comment_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
```

```python
@api_view(['GET', 'POST'])
def comment_list(request, format=None):
    # do stuff...
    
class CommentList(APIView):
    def get(self, request, format=None):
        # do stuff...

    def post(self, request, format=None):
        # do stuff...    
```

DRF를 학습하다보면 `urls.py`에서  `format_suffix_patterns` 라는 함수가 보이는데
해당 함수는 접미사 관련 처리를 해주는 함수이다.

예를 들면 URL에서 Json을 받아오려면 실제로는 `http://example.com/api/users.json` 라고 json임을 표현해줘야하지만, 이 방식이 오류가 발생하기 쉽기 때문에 `http://example.com/api/users` 까지만 해도 json에 접근가능하게 해주는 느낌이다.

중요한것은 `DefaultRouter` 에서는 기본적으로 제공하는 기능이므로 알아만 두면 될 것 같다.
# **Renderer**



DRF에서는 다양한 미디어 유형으로 응답을 반환할 수 있는 렌더러 클래스를 지원한다.



### 기본 설정



```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}
```



렌더러의 기본 설정은 위와 같다.



```python
# views.py
from rest_framework.renderers import JSONRenderer

class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        user_count = User.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content)
```



또한, 위의 예시처럼 개별 클래스에만 렌더러 클래스를 지정할 수도 있다.



### JSONRenderer



utf-8  인코딩을 사용하여 데이터를 JSON으로 렌더링한다.



`.media_tpye` : application/json

`.format` : json

`.charset` :  None



### BrowsableAPIRenderer

브라우저 API 용 HTML로 데이터를 렌더링한다.



`.media_tpye` : text/html

`.format` : api

`.charset` :  utf-8

`.template` : rest_framework/api.html



### TemplateHTMLRenderer

지정한 템플릿으로 데이터를 렌더링한다.

`.media_tpye` : text/html

`.format` : api

`.charset` :  utf-8

`.template` : `template_name ` 에서 지정한 템플릿



```python
class UserDetail(generics.RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    queryset = User.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'user': self.object}, template_name='user_detail.html')
```





### 기타 Renderer



- StaticHTMLRenderer
- AdminRenderer
- MultiPartRenderer



### 타사 패키지



- YAML
- XML
- JSONP
- MessagePack
- excel
- CSV
- UltraJSON
- CamelCase JSON
- Pandas (CSV, Excel, PNG)
- LaTeX










# Throttling




스로틀링은 보통 전자기기에서 기기의 수명이나 안정성을 위해 성능을 의도적으로 제한하는 행위이다.



DRF에서 스로틀링도 비슷한 개념이다.



시스템으로 오는 요청의 수가 과도하게 많을 경우 시스템 전체에 부하가 걸리므로 이를 방지하기 위해 요청 수를 의도적으로 제한하는 것을 스로틀링이라고 한다.



흔히 오픈API를 사용할때 1분당 요청수가 제한되어있는 것이 스로틀링의 개념이라고 볼 수 있다.



또한, 과도한 요청으로 시스템을 공격하는 것을 방지하는 것에도 도움이 될 것이다.



다만 이 경우에는 분산 서비스 거부 공격, 흔히 DDOS라 불리는 공격을 방어하는 것이 불가능하다.



예를 들어서 IP당 100회의 요청만 받는 스로틀링이 걸린 웹사이트가 있다고 해보자.



서비스 공격을 하기 위해 한 컴퓨터로 100000번의 요청을 보낸다면 100회까지만 응답 후 요청이 거부당해서 서비스를 보호할 수 있다. 



그러나 1000대의 컴퓨터로 각각 100회의 요청을 보내면 같은 100000번의 요청일지라도 스로틀링을 모두 통과하여 서버에 공격을 가할 수 있기 때문이다.





### DRF에서 스로틀링 사용하기 (기본 제공)





```python
#settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }  

}
```



- `AnonRateThrottle` : 인증 요청에는 제한이 없으나, 비인증 요청에는 IP 단위로 횟수 제한, 기본 scope  `anon`
- `UserRateThrottle` :  인증 요청에는 유저 단위 횟수를 제한하고, 비인증 요청에는 IP 단위로 횟수 제한, 기본 scope `user`
- `ScopedRateThrottle` : 인증 요청에는 유저 단위 횟수를 제한하고, 비인증 요청에는 IP 단위로 횟수 제한, 각 APIView 별로 서로 다른 scope 적용 가능하다.



```python
# views.py
from rest_framework.throttling import UserRateThrottle

class Task_ViewSet(ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    throttle_classes = [UserRateThrottle]
```



### 커스텀





```python
# views.py
from rest_framework.throttling import UserRateThrottle
from rest_framework.throttling import BaseThrottle

class TestThrottle(BaseThrottle):
    scope = 'anon' # 범위 지정
    def allow_request(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return False
        return super().allow_request(request, view)


class Task_ViewSet(ModelViewSet):
    
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    throttle_classes = [TestThrottle]
```


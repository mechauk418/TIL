

# django-allauth, dj-rest-auth 차이



django-allauth는 django에서 인기있는 인증패키지 중 하나이다.

인증, 등록, 계정 관리 및 소셜 계정 인증 등을 처리한다.

그러나 DRF와 함께 사용할 수 있는 기본 기능을 제공하지 않는다.

즉 Django를 통한 (소셜)인증을 위한 패키지이나, REST API 기능이 없다.

dj-rest-auth는 allauth를 기반으로 하는 패키지이다.

DRF로 인증을 사용하는 것과 격차를 줄여 REST API 엔드포인트를 사용하게 해준다.


![](https://velog.velcdn.com/images/mechauk418/post/b82671f3-63df-4e50-a0ff-9b736b562325/image.jpg)

allauth에서 지원하는 인증

![](https://velog.velcdn.com/images/mechauk418/post/55882792-e3ee-47fd-a714-e6d307543619/image.jpg)

dj-rest-auth에서 제공하는 인증 관련 엔드포인트 (drf를 하면서 흔히 보던 UI)
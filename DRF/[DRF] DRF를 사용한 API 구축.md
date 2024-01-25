# DRF를 사용한 API 구축





### DRF 프로젝트 구조와 코드 조직화



```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    app1/
        migrations/
        __init__.py
        admin.py
        models.py
        serializers.py
        views.py
        urls.py
    app2/
        ...
    app3/
    	...
```



DRF 프로젝트는 일반적으로 위와 같은 구조를 가진다.



### 재사용 가능하고 모듈화된 코드



1. DRF의 일반 뷰와 뷰셋 사용
2. 재사용 가능한 시리얼라이저 생성
3. 일반 기능을 위한 mixin 사용



### 코딩 스타일과 규칙 따르기



코드의 가독성 및 사후 관리를 위해 Python 스타일 가이드인 PEP 8과 Django의 코딩 스타일을 따라야 한다.



### 효율적인 API 디자인과 최적화

1. DRF의 페이지네이션 활용 : 응답에 전송되는 데이터 양을 제어하여 서버 부하를 줄이고 응답 시간을 개선
2. 데이터베이스 쿼리 최적화 : `select_related`와 `prefetch_related` 메서드를 사용하여 쿼리 최적화
3. 캐싱 활용 : 비용이 많이 들거나 자주 사용되는 작업의 결과를 캐싱하여 성능 향상
4. API 쓰로틀링 적용 : 응답 횟수를 제한하여 서버가 오버로드되는 것을 방지


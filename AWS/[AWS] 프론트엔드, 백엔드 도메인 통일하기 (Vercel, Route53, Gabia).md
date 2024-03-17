

# [AWS] 프론트엔드, 백엔드 도메인 통일하기 (Vercel, Route53, Gabia)



제목 그대로 프론트엔드, 백엔드의 도메인을 통일하려고 한다.

이렇게 하는 이유는 보기 깔끔한 것도 있고, 백엔드와 프론트엔드 사이의 쿠키 공유를 위한 것도 있다.

목표하고자 하는 구성은 다음과 같다.

예를 들어서 `example.com` 이라는 도메인을 구매했다고 하자.

백엔드 : `api.example.com`

프론트엔드 : `www.example.com`

이렇게 프론트엔드, 백엔드 도메인을 구성하는 것이 목표이다.

우선 아래의 포스트를 참고하여 백엔드를 메인 도메인에 연결해준다

[백엔드와 도메인 연결](https://velog.io/@mechauk418/DRF-AWS-Elastic-Beanstalk-Github-actions-%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EB%B0%B0%ED%8F%AC-Django-3)

연결이 끝났다면 Route53의 호스팅 영역으로 들어간다.

![](https://velog.velcdn.com/images/mechauk418/post/752ed9e2-d193-4bba-8729-a4ad982d8c3b/image.jpg)

호스팅영역에서 위 사진에 표시된 두 개의 레코드를 생성해준다.

백엔드는 `api.example.com`으로 생성하고 트래픽 대상을 메인 도메인(백엔드)로

프론트엔드는 `www.example.com` 으로 생성하고 트래픽 대상을 프론트엔드 주소로 연결해준다.

![](https://velog.velcdn.com/images/mechauk418/post/8517494b-872e-4a21-85ea-3027c691b1e8/image.jpg)

마지막으로 vercel의 도메인으로 가서 `www.example.com` 프론트엔드 주소를 입력해주면 끝난다.
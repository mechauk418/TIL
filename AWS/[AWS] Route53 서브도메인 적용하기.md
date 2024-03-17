

# [AWS] Route53 서브도메인 적용하기



서브도메인이란?

웹사이트의 섹션을 구분하기 위해 도메인 이름을 구분하는 것이다.

만약 `example.com` 이라는 도메인이 있을때 `shop.example.com`, `article.example.com` 등등 `*.example.com` 의 형식으로 사용한다.

메인도메인을 Route53에서 연결했더라도 서브도메인을 사용하기 위해서는 따로 등록을 해주어야한다.

Route53의 호스팅영역으로 들어간다.

![](https://velog.velcdn.com/images/mechauk418/post/0832cbca-6077-478f-9dd8-d1b1acfea6d0/image.jpg)

위와 같은 화면에서 레코드 생성으로 들어간다.

![](https://velog.velcdn.com/images/mechauk418/post/81b8f3c6-0dfc-479f-8377-f668ec5498d5/image.jpg)

레코드이름에는 서브도메인을 입력하고, 레코드 유형은 CNAME, 값으로는 호스팅 영역의 이름을 넣어주면 된다.
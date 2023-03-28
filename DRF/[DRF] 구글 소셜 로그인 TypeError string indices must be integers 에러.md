# [DRF] 구글 소셜 로그인 TypeError: string indices must be integers 에러



![](https://velog.velcdn.com/images/mechauk418/post/68a70719-113b-4828-8cb8-d2bf41ff5bf6/image.jpg)


구글 소셜로그인 복습중에 

`TypeError: string indices must be integers` 라는 에러가 발생하였다.

인덱스에 정수형을 넣지 않아서 발생하는 오류인데

똑같이 코드를 작성했음에도 배포사이트에선 오류가 없던 것이 새로 코드를 작성하니 오류가 발생한다..


![](https://velog.velcdn.com/images/mechauk418/post/10ed4f90-50c0-46f0-a983-85348aee5caf/image.jpg)


여기까지 오는걸로 봐서는 마지막에 data를 입력해주는 과정에서 500에러가 발생하는 것 같다.

기존 코드랑 비교해서 원인을 찾아봐야겠다.


------------------------------------------------------------------------------

한참을 헤매다가 `django-allauth` 패키지 버전 0.52.0에서 0.51.0으로 다운그레이드하니까 통과되었다.


`allauth` 릴리즈노트를 찾아보았다.

```
0.52.0 (2022-12-29)
Note worthy changes
- Officially support Django 4.1.
- New providers: OpenID Connect, Twitter (OAuth2), Wahoo, DingTalk.
Introduced a new provider setting OAUTH_PKCE_ENABLED that enables the PKCE-enhanced Authorization Code Flow for OAuth 2.0 providers.
- When ACCOUNT_PREVENT_ENUMERATION is turned on, enumeration is now also prevented during signup, provided you are using mandatory email verification. There is a new email template (templates/account/email/acccount_already_exists_message.txt) that will be used in this scenario.
- Updated URLs of Google's endpoints to the latest version; removed a redundant userinfo call.
- Fixed Pinterest provider on new api version.
```

DRF로 프로젝트를 12월 12일에 종료했는데 그사이 버전이 업데이트되서 기존 코드가 오류를 발생시킨 것이였다.

구글의 엔드포인트를 업데이트했다고 한다. 그래서 카카오 로그인에서는 문제가 없었는데 구글 로그인만 오류가 발생한 것이였다.


![](https://velog.velcdn.com/images/mechauk418/post/8ea74d60-b660-45ca-9cf0-26b8122054d3/image.jpg)

allauth 라이브러리를 찾아보니 `googleOAuth2Adapter` 클래스가 이렇게 바뀌었다.

print를 찍어보니 `response` 가 문자열로 나와서 그 아래줄에 `response["id_token"]` 에서 인덱싱 오류가 발생한 것이였다.

해결방안을 더 생각해봤는데 도저히 찾지 못해 당분간은 버전을 내려서 쓸수밖에 없을 것 같다.
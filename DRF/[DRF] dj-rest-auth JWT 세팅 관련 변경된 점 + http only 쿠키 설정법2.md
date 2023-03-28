# [DRF] dj-rest-auth JWT 세팅 관련 변경된 점 + http only 쿠키 설정법2



보안을 위해 refresh token을 http only 쿠키로 만들기 위해 다양하게 시도해보고 있다.

[[DRF] dj-rest-auth JWT 세팅 관련 변경된 점 + http only 쿠키 설정법](https://velog.io/@mechauk418/DRF-dj-rest-auth-JWT-%EC%84%B8%ED%8C%85-%EA%B4%80%EB%A0%A8-%EB%B3%80%EA%B2%BD%EB%90%9C-%EC%A0%90-http-only-%EC%BF%A0%ED%82%A4-%EC%84%A4%EC%A0%95%EB%B2%95)

여기까지 문제점은 백엔드-프론트엔드 사이에 쿠키 전달이 안되는 것이였는데

axios 헤더에서 `withCredentials :true` 를 넣어줘서 백-프론트 간에 쿠키 전달을 구현했다.


![](https://velog.velcdn.com/images/mechauk418/post/6612994b-4c16-4799-b1ee-f3de5429278c/image.gif)


프론트에서 로그인하면 refresh token이 담긴 http only 쿠키를 생성한다.

![](https://velog.velcdn.com/images/mechauk418/post/f8b42c6d-c0ce-48df-822b-36a2237bec41/image.gif)

스크립트로 토큰을 따로 조작하지 않아도 토큰을 refresh 하는 api로 post를 하면 refresh tokne이 전송되어 토큰을 갱신시켜준다.
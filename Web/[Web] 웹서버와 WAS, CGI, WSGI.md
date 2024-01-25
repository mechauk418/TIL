# [Web]  웹서버와 WAS, CGI, WSGI





애플리케이션을 만드는 것도 중요하지만 배포과정도 중요한데 이 부분에서 너무 취약하다는 것을 느끼고 정리해보았다.

### 웹서버

![](https://velog.velcdn.com/images/mechauk418/post/f78a1555-e94e-4fda-ab9b-596c1a2d0f8c/image.svg)

웹서버란 하드웨어 측면에서는 웹서버의 소프트웨어 및 웹사이트의 파일을 저장하는 컴퓨터를 말하며,
소프트웨어 측면에서는 사용자가 접근하는 것을 관리하는 HTTP 서버를 말한다.

초기의 웹 서비스는 간단한 문서 위주의 정적 페이지를 주고받는 수준이였다.

그러나 클라이언트의 요청이 다양해지면서 정적인 페이지에서 구현할 수 있는 한계가 생겼고 자연스럽게 동적 페이지에 대한 관심이 높아졌다.

그래서 등장한게 `WAS(Web Application Server)` 이다.

### WAS (Web Application Server)

WAS는 스크립트를 서버에 저장해놓고 요청이 들어오면 스크립트를 실행하고 그 결과를 반환해주는 미들웨어다.

![](https://velog.velcdn.com/images/mechauk418/post/7f04ad4f-335f-4c69-884c-52ca05b9cd63/image.png)

그림처럼 웹서버가 데이터를 받으면, 컨테이너 내부의 프로그램이 데이터를 처리하고 웹서버에 반환한다.
웹서버는 클라이언트에 데이터를 반환하는 방식이다.



### CGI (Common Gateway Interface)

WAS에서 웹서버와 컨테이너 내부의 프로그램이 데이터를 주고받는다고 했는데, 이 데이터를 주고받는 규칙을 CGI라고 한다.

웹서버나 데이터를 가공하는 프로그램, 스크립트의 종류가 다양하기 때문에 서로 입출력을 표준화하는 것이 필요했고 거기서 나온 것이다.

그러나 CGI는 요청마다 프로그램이 프로세스 단위로 실행된다는 한계점이 있었다.

이러한 한계점때문에 성능이 좋지 못했고 이를 극복하기 위한 확장 CGI인 Servlet나 JSP가 등장했다.

확장 CGI는 프로세스 단위였던 CGI를 스레드 단위로 바꾸고 하나의 거대한 프로세스로 묶은 것을 말한다.

여러 개의 프로세스를 사용하는 방식에서 단일 프로세스를 사용하는 방식으로 변경하여 단점을 보완한 것이다.

### WSGI (Web Server Gateway Interface)

CGI와 비슷한 개념이지만 오직 파이썬을 위한 인터페이스이다.

서버와 애플리케이션으로 나누어져있으며

WSGI 서버에는 `Gunicorn` ,`uwsgi`가 있고

WSGI 애플리케이션에는 우리가 코드를 짜던 `Django`, `Flask`가 있다.

지금까지는 WSGI를 잘 써왔지만 WSGI도 마찬가지로 동기 처리만 가능하다는 한계가 존재했다.


### ASGI (Asynchronous Server Gateway Interface)

위에서 말한 WSGI의 단점을 보완하고자 나온 인터페이스가 바로 ASGI이다.

WSGI와 비슷하지만 비동기 처리가 가능하다는 것이 ASGI만의 특징이다.

ASGI 서버에는 `uvicorn`이 있고

ASGI 애플리케이션에는 `FastAPI` `Django 3.0`이 있다.


### 결론

![](https://velog.velcdn.com/images/mechauk418/post/c4814bd3-9fd0-4255-b533-22a25c140460/image.png)

서버 아키텍처 구성도를 보면 전체적인 흐름을 이해하기 쉽다.
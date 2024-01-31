# [CS] Adapter 패턴



`DRF`의 회원관리 패키지가 Adapter 패턴을 사용하므로 이에 대한 이해도를 위해 정리한다.

### 어댑터 패턴이란

호환성이 없는 기존 클래스의 인터페이스를 변환하여 사용하고자 하는 인터페이스의 형태로 변환시키는 패턴이다.

![](https://velog.velcdn.com/images/mechauk418/post/1901fe49-555b-4f5f-8d99-8e86e9e5fcbe/image.png)

그림에서 보면 `Adaptee`는 `request()` 속성이 없어서 클라이언트가 사용할 수가 없는데

이를 `Target`를 상속하는`Adapter`클래스를 생성하여 여기에서 원하는 인터페이스로 변환시켜주는 것이다.

### 예시

![](https://velog.velcdn.com/images/mechauk418/post/558ed9df-f99d-4587-9912-0f7daa612f7f/image.png)

이해하기 쉽게 풀어준 블로그가 있어서 가져왔다.

기존에 Fighter가 있고, 이를 상속받은 Warrior가 있고, 외부에서 Wizard라는 클래스를 가져와서 적용시키고 싶은 상황이다.

그런데 Wizard는 attack, defend, escape라는 속성은 없고, 이에 대응하는 shot_fire_ball, shield, portal 이라는 속성이 있다.

이런 상황에서 WizardAdapter이라는 Fighter을 상속받은 클래스를 생성하고

```
class WizardAdapter(Fighter):
    def __init__(self, wizard):
        self.wizard = wizard

    def attack(self):
        self.wizard.shot_fire_ball()

    def defend(self):
        self.wizard.shield()

    def escape(self):
        self.wizard.portal()

```

위 코드처럼 원하는 속성으로 변환하면 코드의 변경 없이 새로운 클래스를 추가함으로써 기존과 동일한 인터페이스로 Wizard 클래스를 사용할 수 있게 된다.

이것이 어댑터 패턴이다.

참조 : https://wellsw.tistory.com/240
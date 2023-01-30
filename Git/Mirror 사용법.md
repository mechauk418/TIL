# Mirror 사용법



mirror을 사용하는 이유 : 저장소의 히스토리까지 전부 가져오고 싶을때 사용한다.



A의 저장소에서 내 저장소로 옮기려고 할때



1. 내 git에 새로운 저장소를 만든다

2.  A의 저장소를 가져온다

   ```bash
   git clone --mirror { A의 저장소 주소}
   ```

3.  복사한 저장소의 원격저장소를 나의 원격 저장소로 바꿔준다.

   ```bash
   git remote set-url --push origin { 새로 만든 내 저장소 주소}
   ```

4.  push

   ```bash
   git push --mirror
   ```

   
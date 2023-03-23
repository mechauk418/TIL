

# SQL - DCL



### DDL (Data Control Language)



데이터의 보안, 무결성, 회복, 병행 제어 등을 정의하는데 사용하는 언어

DB관리자가 데이터 관리를 목적으로 사용한다.



| 명령어   | 기능                                                         |
| -------- | ------------------------------------------------------------ |
| COMMIT   | 명령에 의해 수행된 결과를 실제 물리적 디스크에 저장하고 작업이 완료되었음을 관리자에게 알려줌 |
| ROLLBACK | 작업이 비정상적으로 종료되었을 때 원래의 상태로 복구함       |
| GRANT    | DB 사용자에게 사용 권한을 부여함                             |
| REVOKE   | DB 사용자의 사용 권한을 취소함                               |



### GRANT / REVOKE

- DB 사용자에게 사용 권한을 부여하거나 권한을 삭제함.

- 사용자 등급 : DBA (데이터베이스 관리자), RESOURCE (데이터베이스 및 테이블 생성 가능자), CONNECT (단순 사용자)

  ```sqlite
  GRANT RESOURCE TO MINSU;
  
  사용자 ID가 MINSU 인 사람에게 RESOURCE 등급을 부여함.
  ```

  

- 권한 종류 : ALL, SELECT, INSERT, DELETE, UPDATE
- WITH GRANT OPTION : 부여받은 권한을 다른 사람에게 다시 부여 가능한 권한
- GRANT OPTION FOR : WITH GRANT OPTION 권한을 취소함.





### COMMIT / ROLLBACK



- COMMIT 는 작업을 DB에 반영하는 것이다.



- ROLLBACK는 아직 COMMIT되지 않은 작업을 취소하고 이전 상태로 되돌리는 것이다.



- SAVEPOINT는 작업 내에 ROLLBACK 저장점을 지정하는 명령어이다.



```sqlite
SAVEPOINT S1;
DELETE FROM 학생 WHERE 학번=11111;
ROLLBACK TO S1;
```


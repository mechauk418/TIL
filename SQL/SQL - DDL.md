

# SQL - DDL



### DDL (Data Define Language)



- DB를 구축하거나 수정할 목적으로 사용하는 언어



| 명령어 | 기능                                             |
| ------ | ------------------------------------------------ |
| CREATE | SCHEMA, DOMAIN, TABLE, VIEW, INDEX를 정의 (생성) |
| ALTER  | TABLE 정의를 변경                                |
| DROP   | SCHEMA, DOMAIN, TABLE, VIEW, INDEX를 삭제        |



### CREATE

- CREATE SCHEMA

  - 스키마를 정의

    ```mysql
    CREATE SCHEMA 병원 AUTHORIZATION 김민수;
    
    사용자ID가 '김민수'인 스키마 '병원'을 정의
    ```

<br>

- CREATE DOMAIN

  - 도메인을 정의

    ```mysql
    CREATE DOMAIN GENDER CHAR(1) DEFAULT '남' CONSTRAINT VALID-GENDER CHECK(VALUE IN ('남','여'));
    
    GENDER 도메인을 생성하며, 문자형이고 크기는 1이다.
    GENDER 속성의 기본값은 '남'이다.
    GENDER 속성은 '남','여' 두가지 값만 가질 수 있다.
    ```

<br>

- CREATE TABLE

  - 테이블을 정의

    ```mysql
    CREATE TABLE 병원
    		(이름 VARCHAR(15) NOT NULL,
             코드 CHAR(8),
             학과 CHAR(10),
             위치 CHAR(10),
             시간 TIME,
             설립일 CHAR(10),
             PRIMARY KEY(코드),
             FOREIGN KEY(학과) REFERENCES 학과(학과코드)
             	ON DELETE SET NULL
             	ON UPDATE CASCADE
             CONSTRAINT 설립일제약
             	CHECK(설립일>='1900-01-01'));
             	
    병원 테이블 생성
    이름은 최대 15자, NULL이 올 수 없다.
    시간은 TIME 도메인을 가진다.
    코드는 기본키로 사용된다.
    학과는 학과테이블의 학과코드 속성을 참조하는 외래키이다.
    학과테이블에서 튜플이 삭제되면 NULL 값으로 변경된다.
    튜플이 변경되면 같이 변경된다.
    설립일 속성은 `1900-01-01` 이후의 값만 저장할 수 있다.
    ```

<br>

- CREATE VIEW

  - 뷰를 정의

    ```mysql
    CREATE VIEW MYVIEW AS
    SELECT 이름, 생일
    FROM 학생
    WHERE 주소='부천시';
    
    학생 테이블에서 주소가 부천시인 학생들의 이름, 생일을 MYVIEW라는 뷰로 정의함
    ```

    

<br>

- CREATE INDEX

  - 인덱스를 정의

    ```mysql
    CREATE UNIQUE INDEX 학번_index ON 학생(학번 DESC);
    
    중복을 허용 안하는 특성을 갖는 학번 속성에 대해 내림차순으로 정렬하여
    학번_index 라는 이름으로 인덱스를 정의
    ```

    

- ALTER TABLE

  - 테이블에 대한 정의를 변경

    ```sqlite
    ALTER TABLE 테이블명 ADD 주소 VARCHAR(10);
    
    테이블에 최대 10문자의 주소 속성을 추가함
    
    ALTER TABLE 학생 ALTER 학번 VARCHAR(5) NOT NULL;
    
    학생 테이블의 학번 필드를 최대 5문자, NOT NULL로 변경함.
    
    ALTER TABLE 학생 DROP COLUMN 학번 CASCADE;
    
    학생 테이블의 학번 속성을 삭제함
    ```

    

- DROP

  - 스키마, 테이블 등등 정의한 것을 삭제함

    ```sqlite
    DROP SCHEMA 스키마명 CASCADE or RESTRICT
    DROP TABLE 테이블명
    DROP CONSTRAINT 제약조건명
    
    CASCADE : 제거하는 요소를 참조하는 모든 개체를 함께 제거
    RESTRICT : 참조되는 요소는 제거에서 제외한다.
    ```

    
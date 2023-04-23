# AWS Elastic Beanstalk + Github actions 를 활용한 배포 (Django) - 2



## RDS - PostgreSQL

S3가 파일을 저장하는 스토리지라면 RDS는 데이터를 저장하는 데이터베이스서비스이다.

PostgreSQL은 Oracle DB, MySQL, Microsoft SQL같은 데이터베이스 서비스의 일종으로 개발자가 선호하는 SQL이다. RDS는 다양한 SQL을 지원하지만 여기서는 PostgreSQL을 사용하여 배포를 할 것이다.



1. 검색창에서 RDS로 검색하여 진입한다.

2. 데이터베이스를 생성한다 ( **데이터베이스가 2개이상이면 요금이 발생한다**. )

   ```
   생성 방식 : 표준 생성
   엔진 유형 : postgreSQL
   템플릿 : 프리티어 (무료)
   DB 인스턴스 식별자 : DB 이름 입력
   마스터암호 : DB 비밀번호 입력
   스토리지 할당 : 20GB
   스토리지 자동 조정 활성화 : 체크 해제
   퍼블릭 액세스 : 예
   VPC보안그룹 : 새로 생성
   VPC보안그룹 이름 : VPC보안그룹 이름 입력
   성능 인사이트 켜기 : 체크 해제
   초기 데이터베이스 이름 : 초기 DB 이름 자유 입력 (필수 입력)
   자동 백업 활성화 : 체크 해제
   ```



3. 위의 설정대로 데이터베이스를 생성한다. (5~10분 소요)


4. VPC 보안그룹으로 진입하여 인바운드 규칙을 수정한다.

![](https://velog.velcdn.com/images/mechauk418/post/3f3cf6b0-ab77-4ca3-9cff-30e53d33ff41/image.jpg)
![](https://velog.velcdn.com/images/mechauk418/post/f9b7fe24-403f-4ffa-931c-f08b581a9abd/image.png)

- PostgreSQL - Anywhere-IPv4
- PostgreSQL - Anywhere-IPv6


## Django

```bash
# postgresql 관리 패키지 설치
pip install psycopg2-binary
pip freeze > requirements.txt

```

```python
#settings.py

"""
기존 DATABASES 주석 처리
"""
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

	
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "[RDS 생성시 작성한 데이터베이스 이름]"
        "USER": "postgres",
        "PASSWORD": "[마스터 암호]", # 데이터베이스 생성 시 작성한 패스워드
        "HOST": "[RDS 엔드포인트]", # 코드 블럭 아래 이미지 참고하여 입력
        "PORT": "5432",
    }
}

```

여기까지 설정하고 migate해준다.

```python
python manage.py makemigrations
python manage.py migrate

```


## 환경분리

일부 노출되면 안되는 인자들은 환경변수로 관리할 수 있다.

```git
pip install python-dotenv
```

```python

#settings.py

import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = os.getenv("DEBUG")

if DEBUG == True: 
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

else:   
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_REGION = "ap-northeast-2"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"), # 코드 블럭 아래 이미지 참고하여 입력
            "USER": "mechauk",
            "PASSWORD":  os.getenv("DATABASE_PASSWORD"), # 데이터베이스 생성 시 작성한 패스워드
            "HOST": os.getenv("DATABASE_HOST"), # 코드 블럭 아래 이미지 참고하여 입력
            "PORT": "5432",
        }
    }

```

이런 식으로 DEBUG 값을 수정하여 배포와 로컬 환경을 분리하여 관리할 수 있다.


## VScode PostgreSQL 데이터베이스 연결

1. VScode에서 PostgreSQL을 설치한다.

2. db를 연결한다.


![](https://velog.velcdn.com/images/mechauk418/post/c2f3634a-2108-4c52-924d-191326aefd0c/image.png)

![](https://velog.velcdn.com/images/mechauk418/post/8f8a70ad-47e7-4679-a396-03f62d77ef2f/image.jpg)

![](https://velog.velcdn.com/images/mechauk418/post/14b0ba69-d0b3-46c5-82ff-ee3e465bce9a/image.jpg)

완료시 PostgreSQL의 DB가 채워진다.
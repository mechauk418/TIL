# Django 개발 과정



1. 가상 환경 구축



```bash
$ python -m venv [name] ## 가상 환경 만들기
$ source [name]/Scripts/activate ## 가상 환경 실행
$ deactivate ## 가상환경 종료
$ pip install -r requirments.txt # pip 설치
```



2. django 환경 구축



```bash
$ django-admin startproject [프로젝트 이름] [설치 경로] # 프로젝트 생성
$ python manage.py startapp [앱 이름] # 앱 생성
# 앱을 생성하면 반드시 setting.py - INSTALLED_APPS 에 앱을 추가해준다.
$ python manage.py runserver # 서버 실행
```



3. url 분리



```python
# Project - urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_name/',include('app_name.urls')),
]
```

```python
# app폴더에서 urls.py 생성

from . import views

app_name = 'app_name'  # 앱 이름 등록

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    ...
]
```



4. Model 정의



```python
# models.py 작성 (클래스 정의)

class Articles(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
```

```bash
$ python manage.py makemigrations # migrations 생성
$ python manage.py migrate # migrate (DB 반영)
```









5. CRUD 기능 구현 (views 작성)



1) 게시글 생성

   <br>

   - forms.py<br>

   이와같은 구조를 통해 Validation 및 코드를 간소화할수있다.

   ```python
   # app - forms.py 생성
   
   from django import forms
   from .models import Article # 작성한 모델 import
   
   class ArticleForm(forms.ModelForm):
       
       class Meta:
           model = Article     # Article 에 있는 
           fields = '__all__'  # 모든 필드를 쓴다
           fields = ['title','content'] # title과 content 만 쓴다.
           
           
   # templates에서 받을때
       
   {{ name.as_p}}
   ```

   

   - urls.py<br>

   ```python
   urlpatterns = [
       path("", views.index, name="index"),
       path("new/", views.new, name="new"), # new url 추가
   ]
   ```

   - views.py<br>

   ```python
   def create(request):
       # POST method를 받아옴
       if request.method == 'POST':
   
           articleForm = ArticleForm(request.POST)
           # 유효성 검사를 통과하면 저장 후 리다이렉트
           if articleForm.is_valid():
               articleForm.save()
   
               return redirect('test_app:index')
       # 입력을 받기 전에는 그냥 Form 출력
       else:
           articleForm = ArticleForm()
       context={
           'articleForm': articleForm
       }
   
       return render(request, 'test_app/new.html', context=context)

<br>

2. 게시글 목록

   <br>

   - views.py<br>

   ```python
   
   def index(request):
   
       # 모든 Articles 요소를 pk순으로 정렬하여 불러옴
       articles = Articles.objects.order_by('pk')
   
       context = {
           "articles" : articles,
       }
   
       return render(request,'test_app/index.html',context )
   ```

   <br>

   - index.html<br>

   ```html
   <body>
         게시글 목록
   
         {% for article in articles %}
     <div>
       번호: {{ article.id }}
       <br>
       제목: {{ article.title}}<br>
       내용: {{ article.content}}
       <hr>
     </div>
     {% endfor %}
   </body>
   ```

   <br>

3. 상세보기

   - urls.py<br>

   ```python
   urlpatterns = [
       path("", views.index, name="index"),
       path("new/", views.new, name="new"), 
       # pk를 받아오는 url 추가
       path("detail/<int:pk>", views.detail, name="detail"), 
   ]
   ```

   - views.py<br>

   ```python
   def detail(request,pk): # pk를 인자로 받음
   
       article = Articles.objects.get(pk=pk) # pk=pk인 요소를 선언
       context = {"article":article }
   
   
       return render(request,'test_app/detail.html',context)
   ```

   - detail.html<br>

   ```html
   <body>    
   	<div class="row">
         <h2> {{article.title}}</h2>
       </div>
       <div class="row text-end">
         <h6> 최근 수정: {{ article.updated_at|date:'Y년 m월 d일' }} </h6>
       </div>
   
       <div class="jumbotron">
         <p class="mt-5 border border-3 p-3"> {{article.content }} </p>
       </div>
   </body>
   ```

   <br>

4. 삭제하기

   - views.py

   ```python
   def delete(request,pk):
   	# pk=pk인 요소를 받아와서 삭제함
       article = Articles.objects.get(pk=pk)
       article.delete()
   
       return redirect('test_app:index')
   ```

   <br>

   - detail.html

   ```python
   <div class="m-1">
   	<a href="{% url 'test_app:delete' article.pk   %}">
   	<input type="submit" value="리뷰 수정">
   	</a>
   </div>
   ```

   <br>

5. 수정하기

   - views.py

   ```python
   # 하나의 값을 불러오는 것 외에는 create와 비슷하다.
   
   def edit(request,pk):
       # pk값에 해당하는 요소를 받아옴
       article = Articles.objects.get(pk=pk)
       # POST method를 받아옴
       if request.method == 'POST':
           # 기존 입력된 값을 instance에 그대로 받아옴
           articleForm = ArticleForm(request.POST, instance = article)
           # 유효성 검사를 통과하면 저장 후 리다이렉트
           if articleForm.is_valid():
               articleForm.save()
   
               return redirect('test_app:detail',article.pk)
       # 입력이 안되었으면 
       else:
           articleForm = ArticleForm(instance = article)
       context={
           'articleForm': articleForm
       }
   
       return render(request, 'test_app/edit.html', context=context)
   ```

   <br>

   - edit.html

   ```html
   <body>
     <form action="" method="POST">
       {% csrf_token %}
       {{ articleForm.as_p }}
       <input type="submit" value="수정">
     </form>
   </body>
   ```

   


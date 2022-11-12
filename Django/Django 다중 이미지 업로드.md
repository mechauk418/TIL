# Django 다중 이미지 업로드



Django에서 `<input> multiple` 태그를 활용하여 다중 이미지를 업로드 할 수 있다.



## models.py

```python
class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
```



### create.html (template)

```html
<div class="container my-5">

  <form action="" method="POST" class="" enctype="multipart/form-data">
    {% csrf_token %}
    {% bootstrap_form post_form %}
      <!-- form 내부에 input multiple 를 넣어준다 -->
    <input type="file" name="imgs" multiple> 
    <div class="text-end"><input class="btn btn-primary" type="submit" value="작성"></div>
  </form>
  
</div>
```



## views.py

```python
def create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)        
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            for img in request.FILES.getlist('imgs'):
                # Photo 객체를 하나 생성한다.
                photo = Photo()
                # 외래키로 현재 생성한 Post의 기본키를 참조한다.
                photo.post = post
                # imgs로부터 가져온 이미지 파일 하나를 저장한다.
                photo.image = img
                # 데이터베이스에 저장
                photo.save()

            return redirect("posts:index")

    else:
        post_form = PostForm()

    context = {
        "post_form": post_form,
    }

    return render(request, "posts/create.html", context)
```



## detail.html (템플릿에서 이미지 사용하기)

```html
{% if post.photo_set %} # 분기처리
    {% for photo in post.photo_set.all %}
		<img src="{{ photo.image.url }}" alt="{{ photo.image.image }}">
	{% endfor %}
{% else %}
{% endif %}
```









참고 : https://dheldh77.tistory.com/entry/Django-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%97%85%EB%A1%9C%EB%93%9C






# 간단한 Django 무한스크롤



JS를 잘 몰라서 쉽게 무한스크롤을 구현하는 방법을 찾다가 `Waypoints` 라는 라이브러리에 대해 알게 되었다.



http://imakewebthings.com/waypoints/  - 다운로드 링크

http://imakewebthings.com/waypoints/shortcuts/infinite-scroll/ - 무한스크롤 링크



**base.html**

```html
<script src="{% static 'js/jquery.waypoints.min.js' %}"></script>
<script src="{% static 'js/infinite.min.js' %}"></script>
```

static으로 `waypoints` 파일을 불러온다. (jquery도 있어야한다.)

static 경로는 .js 파일이 저장된 위치로 변경한다.



**index.html**

```html
<div class="infinite-container"> 
{% for post in page_obj %}
  <div class="infinite-item">{{post.title}}</div>
{% endfor %}
</div>

{% if page_obj.has_next %}
<a class="infinite-more-link" href="/next/page">More</a>
{% endif %}

...



<script>
    var infinite = new Waypoint.Infinite({
        element: $('.infinite-container')[0],

        offset: 'bottom-in-view',

        onBeforePageLoad: function () {
            $('.loading').show();
        },
        onAfterPageLoad: function () {
            $('.loading').hide();
        }

    });

</script>
```



`infinite-container`  내부에 반복문을 넣어주고 반복되는 아이템을`infinite-item` 으로 설정한다.



`onBeforePageLoad`, `onAfterPageLoad` 에 `show()`, `hide()` 를 넣어주면 시각적인 효과를 낼 수 있다.



**views.py**

```python
from django.core.paginator import Paginator

def index(request):

    posts = Post.objects.all()
    page = request.GET.get('page') 
    paginator = Paginator(posts, '3') # (분할하는 객체, 페이지 당 갯수 )
    page_obj = paginator.get_page(page)
    
    context={
        "page_obj":page_obj,
    }
    return render(request,"posts/index.html",context)


```



`views.py` 에서는 Django의 페이지네이션 도구인 `Paginator` 을 활용한다.

`    page = request.GET.get('page') ` : `page`라는 변수에 요청의 page값을 읽어온다.

`    paginator = Paginator(posts, '3')` : `paginator`이라는 객체에 분할하는 객체, 페이지 당 갯수를 입력한다.

`page_obj = paginator.get_page(page)` : `paginator` 객체에서 요청으로 받아온`page` 부분만을 보여주는 객체이다.



참고 : https://taehyeki.tistory.com/265
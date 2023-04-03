

# [DRF] Nested Serializer (serializer 중첩)



`Nested Serializer` 는 Serializer를 중첩시키는 것을 말한다.

Serializer을 중첩시키는 이유는 서로 다른 DB에 있는 데이터를 하나로 묶어서 응답하거나, 1:N 데이터를 표현하기 위해서이다.

### 코드

```python
# models.py

class Tag(models.Model):
    name = models.CharField(max_length=80)

class Category(models.Model):
    name = models.CharField(max_length=80)
```

```python

# serializer.py

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class CateTagSerializer(serializers.Serializer):
    cateList = CategorySerializer(many=True)
    tagList = TagSerializer(many=True)


```

위에서 정의한 Serializer을 `CatetagSerializer` 에서 필드로 재사용하고 있다.


```python
# views.py

class CateTagAPIView(APIView):
    def get(self,request,*args,**kwargs):
        cateList = Category.objects.all()
        tagList = Tag.objects.all()

        data = {
            'cateList': cateList,
            'tagList' : tagList,
        }

        serializer = CateTagSerializer(instance=data)

        return Response(serializer.data)

```

view에서 정의할때는 `APIView`를 상속받는다. `genericView`는 단일 테이블일때만 쓸 수 있다.

### 결과

![](https://velog.velcdn.com/images/mechauk418/post/f9ce61e3-95d0-4341-8eb2-55d424e2ab1e/image.jpg)
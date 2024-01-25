

# select_related, prefretch_related



select_related = JOIN을 통해 데이터를 즉시 가져오는 방법

1:1에서나 1:N에서 N이 사용할 수 있다. 정방향 참조 (Post에서 Category를 찾는 방향)



```python
for comment in Comment.objects.all():
    print(comment.post.title)
    
    
```





prefretch_related = 추가 쿼리를 통해 데이터를 즉시 가져오는 방법

1:N에서 1이 사용할 수 있고, M:N에서 사용할 수 있다. 역방향 참조




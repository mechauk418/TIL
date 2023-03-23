from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Article_ViewSet, Comment_ViewSet, LikeCreate

app_name = "articles"

router = DefaultRouter()
router.register('',Article_ViewSet)

urlpatterns = [
    path("",include(router.urls)),
    path(
        "<int:article_pk>/comment/",
        Comment_ViewSet.as_view({"post": "create", "get": "list"}),
    ),
    path(
        "<int:article_pk>/comment/<int:pk>/",
        Comment_ViewSet.as_view(
            {"put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
    ),
    path(
        "<int:article_pk>/like/",
        LikeCreate.as_view(),
    ),

]
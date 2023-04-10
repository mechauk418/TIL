from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Article_ViewSet, Comment_ViewSet, LikeCreate

app_name = "articles"

urlpatterns = [
    path("", Article_ViewSet.as_view({'get':'list', 'post':'create'})),
    path("<int:pk>/", Article_ViewSet.as_view({'get':'retrieve', "delete": "destroy", "put": "update", "patch": "partial_update"})),
    path(
        "<int:pk>/comment/",
        Comment_ViewSet.as_view({"post": "create", "get": "list"}),
    ),
    path(
        "<int:pk>/comment/<int:comment_pk>/",
        Comment_ViewSet.as_view(
            {"put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
    ),
    path(
        "<int:pk>/like/",
        LikeCreate.as_view(),
    ),
]
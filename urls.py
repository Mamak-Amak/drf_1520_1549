from django.contrib import admin
from django.urls import path
from mainapp import views

from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from django.urls import path, include
from mainapp import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('views/api-view/', views.ArticleAPIVIew.as_view()),
    path('generic/retrieve/<int:pk>/', views.ArticleRetrieveAPIView.as_view())
    path('filters/kwargs/<str:name>/', views.ArticleKwargsFilterView.as_view())
]

class ArticleDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

router = DefaultRouter()
router.register('base', views.ArticleViewSet, basename='article')

urlpatterns = [
    path('viewsets/', include(router.urls)),
]
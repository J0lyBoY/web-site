from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main),
    path('create', views.create_news),
    path('<int:pk>', views.NewsDetail.as_view(), name='news-detail'),
]

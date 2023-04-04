from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('exhibition', views.exhibition),
    path('panoram_view', views.panoram_view),
    path('people_photos', views.people_photos),
    path('exhibition_photos', views.exibition_photo),
]

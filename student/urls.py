from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.get_post_students, name='get_post_students'),
    path('add-mark/', views.get_post_marks, name='get_post_marks'),
    path('results/', views.get_results, name='get_results'),
]

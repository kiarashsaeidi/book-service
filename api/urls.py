from django.urls import path
from . import views

urlpatterns = [
    path('api/book/<int:id>/', views.bookDetail, name='book_detail'),
    path('api/test', views.test, name='test'),
]
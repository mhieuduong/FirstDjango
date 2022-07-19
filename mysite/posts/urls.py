from django.urls import path
from posts import views
# from . import views

app = 'posts'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
]

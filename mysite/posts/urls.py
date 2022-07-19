from django.urls import path
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns

app = 'posts'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
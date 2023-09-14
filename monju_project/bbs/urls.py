from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('new', views.new, name='new'), # 投稿用WebページのURL
    path('create', views.create, name='create'), # 新規投稿をデータベースに保存するためのURL
]

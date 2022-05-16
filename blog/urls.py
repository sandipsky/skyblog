from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>', postDetail, name='detail'),
    path('create/', postCreate, name='create'),
    path('edit/<int:pk>', postUpdate, name='update'),
    path('manage/', postManage, name='manage'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>', postDetail, name='detail'),
    path('create/', postCreate, name='create'),
    path('edit/<int:pk>', postUpdate, name='update'),
    path('manage/', postManage, name='manage'),
    path('delete/<int:pk>', postDelete, name='delete'),
    path('register/', register, name='register'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
]
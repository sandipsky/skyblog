from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>', postDetail, name='detail')
]
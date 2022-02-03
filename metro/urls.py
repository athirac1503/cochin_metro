from django.urls import path
from. import views
urlpatterns=[
    path('index/',views.fnIndex,name='index/'),
    path('home/',views.fnHome,name='home/')
]
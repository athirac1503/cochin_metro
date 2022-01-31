from django.urls import path
from. import views
urlpatterns=[
    path('index/',views.fnIndex,name='index/')
]
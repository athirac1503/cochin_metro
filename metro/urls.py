from django.urls import path
from. import views
urlpatterns=[
    path('login',views.fnLogin,name='login'),
    path('home/',views.fnHome,name='home/'),
    path('signup/',views.fnSignup,name='signup/')
]
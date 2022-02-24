from django.urls import path
from. import views
urlpatterns=[
    path('login',views.fnLogin,name='login'),
    path('home',views.fnHome,name='home'),
    path('signup',views.fnSignup,name='signup'),
    path('station',views.fnStation,name='station'),
    path('index',views.fnIndex,name='index'),
    path('ticket',views.fnTicket,name='ticket'),
    path('contact',views.fnContact,name='contact'),
    path('contact1',views.fnContact1,name='contact1'),
    path('about',views.fnAbout,name='about'),
    path('price',views.fnPrice,name='price')
]
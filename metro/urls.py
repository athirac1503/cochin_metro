from django.urls import path
from .import views

urlpatterns = [
    path('', views.new, name='new'),
    path('index', views.index, name='index'),
    path('main', views.login, name='main'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('station', views.station, name='station'),
    path('ticket', views.ticket, name='ticket'),
    path('contact', views.contact, name='contact'),
    path('contact1', views.contact1, name='contact1'),
    path('about', views.about, name='about'),
    path('price', views.price, name='price'),
    path('ticket1', views.ticket1, name='ticket1'),
    path('ticket2', views.ticket2, name='ticket2'),
    path('index1', views.index1, name='index1'),
    path('payment', views.payment, name='payment'),
    path('otp', views.otp, name='otp'),
    path('otp1', views.otp1, name='otp1'),
    path('payment1', views.payment1, name='payment1'),
    path('qrcode', views.qrcode, name='qrcode'),
    path('travel', views.travel, name='travel'),
    path('logout', views.logout, name='logout'),
    path('uprofile', views.uprofile, name='uprofile'),
    path('upayment', views.upayment, name='upayment'),
    path('track', views.track, name='track')






]

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
    path('about', views.about, name='about'),
    path('price', views.price, name='price'),
    path('ticket1', views.ticket1, name='ticket1'),
    path('ticket2', views.ticket2, name='ticket2'),
    path('index1', views.index1, name='index1'),
    path('qrcode1', views.qrcode1, name='qrcode1'),
    path('travel', views.travel, name='travel'),
    path('logout', views.logout, name='logout'),
    path('uprofile', views.uprofile, name='uprofile'),
    path('upayment', views.upayment, name='upayment'),
    path('track', views.track, name='track'),
    path('train_details', views.train_details, name='train_details'),
    path('change_password', views.change_password, name='change_password'),
    path('user_welcome', views.user_welcome, name='user_welcome'),
    path('message_view', views.message_view, name='message_view')






]

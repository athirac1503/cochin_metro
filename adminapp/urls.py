from django.urls import path
from. import views

urlpatterns=[
        path('admin_login',views.admin_login,name='admin_login'),
        path('fair',views.fair,name='fair'),
        path('add_fair',views.add_fair,name='add_fair'),
        path('update_fair',views.update_fair,name='update_fair'),
        path('complaints',views.complaints,name='complaints'),
        path('train',views.train,name='train'),
        path('ad_logout',views.ad_logout,name='ad_logout'),
        path('add_station_details',views.add_station_details,name='add_station_details'),
        path('aprofile',views.aprofile,name='aprofile'),
        path('reply/<int:id>',views.reply,name='reply'),
        path('hello',views.hello,name='hello'),
        path('welcome',views.welcome,name='welcome')



]
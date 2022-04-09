from django.urls import path
from. import views

urlpatterns=[
        # path('admin_master',views.fair,name='fair'),
        path('fair',views.fair,name='fair'),
        path('rout',views.rout,name='rout'),
        path('complaints',views.complaints,name='complaints'),
        path('train',views.train,name='train'),
        path('ad_logout',views.ad_logout,name='ad_logout'),
        path('ad_station',views.ad_station,name='ad_station'),
        path('aprofile',views.aprofile,name='aprofile'),
        path('reply',views.reply,name='reply')


]
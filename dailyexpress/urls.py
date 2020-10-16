from django.urls import path,include
from. import views

urlpatterns = [
    path('',views.home,name="home"),
    path('bnews',views.bnews,name="bnews"),
    path('enews',views.enews,name="enews"),
    path('hnews',views.hnews,name="hnews"),
    path('scnews',views.scnews,name="scnews"),
    path('snews',views.snews,name="snews"),
    path('tnews',views.tnews,name="tnews"),
    
]

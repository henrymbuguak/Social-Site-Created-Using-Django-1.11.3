from django.conf.urls import url
from account import views as account_views
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', account_views.dashboard, name='dashboard'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$',views.logout, name='logout'),
    url(r'^logout-then-login/$',views.logout_then_login, name='logout-then-login'),
    #url(r'^login/$', views.user_login, name='login'),

]

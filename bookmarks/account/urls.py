from django.conf.urls import url
from account import views as account_views
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', account_views.dashboard, name='dashboard'),
    url(r'^register/$', account_views.register, name='register'),
    url(r'^edit/$', account_views.edit, name='edit'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$',views.logout, name='logout'),
    url(r'^logout-then-login/$',views.logout_then_login, name='logout-then-login'),
    #url(r'^login/$', views.user_login, name='login'),

    #password change urls
    url(r'^password-change/$', views.password_change, name='password_change'),
    url(r'^password-change/done/$', views.password_change_done, name='password_change_done'),

    #reset password urls
    url(r'^password-reset/$', views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', views.password_reset, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', views.password_reset_complete, name='password_reset_complete'),


]

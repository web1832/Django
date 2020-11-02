from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth import views as auth_views
app_name = 'common'


urlpatterns = [
   url('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
   url('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
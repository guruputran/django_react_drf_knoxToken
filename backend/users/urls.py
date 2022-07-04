from django.urls import path #  re_path, include
from .views import RegisterAPI, ManageUserView, PostgetView
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
  path('register',RegisterAPI.as_view(), name='register'),
  path('profile', ManageUserView.as_view(), name='profile'),
  path('mypost', PostgetView.as_view(), name='post'),
  path('login', LoginAPI.as_view(), name='login'),
  path('logout', knox_views.LogoutView.as_view(), name='logout'),
  path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
  # re_path(r'apik/auth/', include('knox.urls')),
]

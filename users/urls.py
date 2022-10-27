from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update_user, name='update'),
]
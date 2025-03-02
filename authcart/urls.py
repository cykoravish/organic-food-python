from django.urls import path
from authcart import views

urlpatterns = [  # Fixed typo
    path('signup/', views.signupviews, name='signup'),
    path('login/', views.handlelogin, name='handlelogin'),  # Fixed function name
    path('logout/', views.handlelogout, name='handlelogout'),
  
]

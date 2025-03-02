from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),  
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('blog/', views.blog_list, name='blog_list'),  # List of blog posts
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('reviews/', views.review_page, name='review_page'),
    path('Feature/', views.Feature, name='Feature'),
    path('checkout/', views.checkout, name="Checkout"),
    path('contact/', views.contactview, name='contact'),
    
    
]

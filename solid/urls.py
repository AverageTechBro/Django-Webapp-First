from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.starter, name='starter'),
    path('watches/<int:id>', views.watch, name='watches'),
    path('login/', views.login_user, name='login'),
    path('', views.homeRedirect, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('blog/<int:id>', views.blog_page, name='blog'),
    path('profile-pic/', views.avatarView, name='profile-pic'),
    path('create-blog/', views.create_blog, name='createBlog'),
    path('blog-home/', views.blog_home, name='blogHome'),
    path('watch-add/', views.home_watch, name='homeAdd'),

]

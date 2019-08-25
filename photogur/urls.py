from django.contrib import admin
from django.urls import path
from photogur import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root),
    path('pictures/', views.pictures_view),
    path('pictures/<int:id>', views.picture_show, name='picture_details'),
    path('search/', views.picture_search, name='picture_search'),
    path('comments/new', views.create_comment, name='create_comment'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('pictures/new', views.picture_new, name="picture_new"),
    path('pictures/create', views.picture_create),
    path ('edit', views.edit_picture, name="edit_picture"),
]
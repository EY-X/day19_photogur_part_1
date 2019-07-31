from django.contrib import admin
from django.urls import path
from photogur import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pictures/', views.pictures_view),
    path('pictures/<int:id>', views.picture_show, name='picture_details'),
    path('search/', views.picture_search, name='picture_search'),
    path('comments/new', views.create_comment, name='create_comment'),
]

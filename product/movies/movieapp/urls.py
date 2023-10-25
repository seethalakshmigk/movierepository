from unicodedata import name
from django.urls import path
from . import views
app_name='movieapp'


urlpatterns = [
    path('', views.index, name="index"),
    path('details/<int:id>/', views.show_details, name="detail"),  # Use name="detail"

    path('add/',views.add_movies,name="addmovie"),
    path('edit/<int:movie_id>/', views.update_movies, name="update"),

    path('delete/<int:id>/', views.delete, name='delete'),



]



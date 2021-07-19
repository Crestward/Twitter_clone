from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('<str:username>/', views.ProfileDetailView.as_view(), name = 'profile'),
    path('<str:username>/follow', views.FollowView.as_view(), name = 'follow'),

]
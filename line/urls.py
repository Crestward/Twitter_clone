from django.urls import path

from . import views

app_name = 'line'

urlpatterns = [
    path('', views.HomePage.as_view(), name = 'home'),
    path('<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
    path('new/', views.CreateNewPost.as_view(), name = 'new_post'),
    path('signup/', views.RegisterFormView.as_view(), name = 'sign_up'),

]
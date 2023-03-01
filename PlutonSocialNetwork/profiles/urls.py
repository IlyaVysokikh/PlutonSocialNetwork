from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserLoginView.as_view()),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('dev', views.DevPageView.as_view(), name='dev'),
    #path('id', )
]
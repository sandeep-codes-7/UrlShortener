from django.urls import path #type: ignore
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('result/',views.result,name='result'),
    path('<str:redir>',views.redirect_url,name='redirect_url'),
]
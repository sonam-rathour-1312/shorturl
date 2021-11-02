from django.urls import path
from .views import home, redirect_url_view

appname='shorty'

urlpatterns = [
    path("",home, name='home'),
    path('<str:shortened_part>', redirect_url_view, name='redirect')
]

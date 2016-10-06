from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.user_login, name="login"),
    url(r'^app/$', views.startpage),
    url(r'^registration/$', views.user_registration, name="registration"),
    url(r'^registration/validate@username=(?P<username>([a-zA-Z\d]+)|\.)@email=(?P<email_address>\.|([_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)+))$', views.validate)
]

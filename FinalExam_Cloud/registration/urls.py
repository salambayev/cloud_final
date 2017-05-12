from django.conf.urls import url

from .views import reg_view, log_view, logout_view

urlpatterns = [
    url(r'^register/$', reg_view, name='register'),
    url(r'^login/$', log_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
]
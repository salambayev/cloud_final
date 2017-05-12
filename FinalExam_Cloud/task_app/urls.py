from django.conf.urls import url

from .views import get_tasks

urlpatterns = [
    url(r'^$', get_tasks, name='index'),
]


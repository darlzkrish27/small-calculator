from django.conf.urls import include, url
from .views import SumView

urlpatterns = [
    url(r'^$', SumView.as_view(), name='sum')
]

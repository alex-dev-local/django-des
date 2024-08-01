from django.urls import re_path as url
from des import views


urlpatterns = [
    url("send-test-email/", views.send_test_email, name = 'des-test-email'),
]

__all__ = ['urlpatterns']

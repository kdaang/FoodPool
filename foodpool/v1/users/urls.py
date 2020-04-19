from django.conf.urls import url
from foodpool.v1.users.views import DeliveryAddressAPIView

app_name = 'users'

urlpatterns = [
    url(r'^address/?$', DeliveryAddressAPIView.as_view()),
]
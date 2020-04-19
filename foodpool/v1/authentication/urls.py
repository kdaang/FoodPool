from django.conf.urls import url
from foodpool.v1.authentication.views import RegistrationAPIView, LoginAPIView

app_name = "authentication"

urlpatterns = [
    url(r'^register/?$', RegistrationAPIView.as_view()),
    url(r'^login/?$', LoginAPIView.as_view()),
]
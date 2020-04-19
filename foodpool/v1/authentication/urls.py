from django.conf.urls import url
from foodpool.v1.authentication.views import RegistrationAPIView

app_name = "authentication"

urlpatterns = [
    url(r'^register/?$', RegistrationAPIView.as_view()),
]
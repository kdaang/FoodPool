from django.conf.urls import url

from foodpool.v1.menus.views import RestaurantAPIView

app_name = "menus"

urlpatterns = [
    url(r'^restaurants/?$', RestaurantAPIView.as_view()),
]
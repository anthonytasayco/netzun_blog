from django.conf.urls import url
from rest_framework import routers
from .views import PublicationAPIList, home


router = routers.SimpleRouter()

urlpatterns = [
	url(r"^api_v1/$", PublicationAPIList.as_view(), name="publication_list"),
	url(r"^$", home, name="home"),

    ]

urlpatterns += router.urls

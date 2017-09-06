from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from main.views import UserViewset
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('users', UserViewset )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^new', include('new.urls', namespace='new_app'))

]

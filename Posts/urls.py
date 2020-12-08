from django.urls import path 
from Posts.views import PostsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', PostsViewSet)
urlpatterns = router.urls
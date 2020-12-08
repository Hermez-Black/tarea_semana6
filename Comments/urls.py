from django.urls import path 
from Comments.views import CommentsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', CommentsViewSet)
urlpatterns = router.urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ActivateAccountView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('activate/<str:uid>/<str:token>/', ActivateAccountView.as_view(), name='activate_account'),
    path('', include(router.urls)),
]

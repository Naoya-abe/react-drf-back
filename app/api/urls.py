from django.urls import path, include
from rest_framework import routers

from api.views import TaskViewSet, UserViewSets, ManageUserView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('users', UserViewSets)

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls))
]

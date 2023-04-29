from Api_Todo.views import task_readAll_create, task_detail_update_delete_id
from Api_Todo.views import TaskAPIViewListCreate, TaskAPIViewDetailChangeDelete
from Api_Todo.views import TaskViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TaskViewSet, basename='Tasks')

urlpatterns = [
    path('v1/', task_readAll_create),
    path('v1/<int:pk>/', task_detail_update_delete_id),
    path('v2/', TaskAPIViewListCreate.as_view()),
    path('v2/<int:pk>/', TaskAPIViewDetailChangeDelete.as_view()),
    path('v3/', include(router.urls)),
]
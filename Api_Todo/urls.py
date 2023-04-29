from Api_Todo.views import task_readAll_create, task_detail_update_delete_id

from django.urls import path

urlpatterns = [
    path('', task_readAll_create),
    path('<int:pk>/', task_detail_update_delete_id)
]
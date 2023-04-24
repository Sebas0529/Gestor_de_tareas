# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from task import views as task_views 


urlpatterns = [
    path('create_task/', task_views.userCreatetaskView.as_view()),
    path('list_task/', task_views.listtaskView.as_view()),
    path('update_task/', task_views.updatetaskView.as_view()),
    path('delete_task/', task_views.deletetaskView.as_view()),
    path('filter_status_task/', task_views.filterstatusView.as_view()),
    path('filter_admin_task/', task_views.filterusertask.as_view()),
]
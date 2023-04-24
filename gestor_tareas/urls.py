from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login-register/', include(('users.urls', 'users'), namespace='users')),  
    path('tasks/', include(('task.urls', 'task'), namespace='task')),
]

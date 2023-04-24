# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from users import views as user_views

#router = DefaultRouter()
#router.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
    #path('', include(router.urls)),
    path('login/', user_views.UserloginView.as_view()),
    path('create/', user_views.UsercreateView.as_view()),
    path('list/', user_views.UserlistView.as_view()),
    path('usuario/', user_views.userfilterView.as_view()),
    path('delete_user/', user_views.deletetaskView.as_view()),
    
]
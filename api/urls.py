from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')


urlpatterns = [
    path('list-tag/', views.TagListView.as_view(), name='list-tag'),
    path('detail-tag/<str:pk>/', views.TagRetrieveView.as_view(), name='detail-tag'),
    path('list-task/', views.TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>/',
         views.TaskRetrieveView.as_view(), name='detail-task'),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login-user/', views.LoginUserView.as_view(), name='login-user'),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.jwt'))
]

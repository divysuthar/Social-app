from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    # path('recent-comments/', views.recent_comments, name='recent_comments'),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
]

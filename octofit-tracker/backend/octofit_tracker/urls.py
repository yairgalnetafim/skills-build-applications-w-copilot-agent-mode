
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.http import JsonResponse
import os

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)
router.register(r'workouts', views.WorkoutViewSet)

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    if codespace_name and codespace_name != 'localhost':
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        base_url = "http://localhost:8000"
    return JsonResponse({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/root/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]

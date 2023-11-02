from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "busapp"

urlpatterns = [
    path('feed/', views.feed),
    path('search_bus/', views.search_bus),
    path('result_bus/', views.search_result_bus),
]

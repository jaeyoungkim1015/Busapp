from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "maps"

urlpatterns = [
    path('navigation/', views.navigation),
    path('search/', views.search_place),
    path('result/', views.search_result),
]
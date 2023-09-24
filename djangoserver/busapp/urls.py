from django.urls import path
import busapp.views

app_name = 'busapp'

urlpatterns = {
    path('', busapp.views.main, name='main'),
}

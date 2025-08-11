from django.urls import path
from views import index, latest_data_view
urlpatterns = [
    path('', index, name='index'),
    path('latest', latest_data_view, name='latest'),
]
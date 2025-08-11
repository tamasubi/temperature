from django.shortcuts import render
from .models import SensorData


def index(request):
    return render(request, 'index.html')




def latest_data_view(request):
    latest = SensorData.objects.order_by('-timestamp').first()
    return render(request, 'latest.html', {'data': latest})



# Create your views here.

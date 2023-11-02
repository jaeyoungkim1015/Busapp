from django.shortcuts import render
# Create your views here.


def feed(request):
    return render(request, 'busapp/feed.html')

def search_bus(request):
    return render(request, 'busapp/search_bus.html')

def search_result_bus(request):
    return render(request, 'busapp/search_result_bus.html')
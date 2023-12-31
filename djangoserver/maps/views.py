from django.shortcuts import render

# Create your views here.

def navigation(request):
    #경로 안내
    # 현재 위치 부터 목적지까지 30초 마다 리젠
    # geolocation으로 마커 표시

    #시각장애인을 위한 음성지도 제작에 관한 연구 - 국토지리학회에서 말하길 시각장애인의 보행 속도는 1m/1s 이다
    # 일반인의 보행 속도는 4km/시 = 4000m / 3600s = 1.1m/s 이므로 예상 도착 시간 x 1.11

    try:
        data = {
            "destination_lat": request.GET['destination_lat'],
            "destination_lon": request.GET['destination_lon'],
            "destination_name": str(request.GET['destination_name'])
        }
    except:
        data = {
            "destination_lat": 0,
            "destination_lon": 0,
            "destination_name": "TEST"
        }
    return render(request, 'maps/navigation.html', data)


def search_place(request):
    return render(request, 'maps/search_place.html')

def search_result(request):
    return render(request, 'maps/search_result.html')

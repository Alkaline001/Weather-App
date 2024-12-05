import requests
from django.shortcuts import render
from django.http import JsonResponse


API_KEY = 'https://openweathermap.org/api'

def get_weather(request):
    city = request.GET.get('city', 'London')  #example
    url = f'https://openweathermap.org/api?q={city}&appid={API_KEY}&units=metric'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return render(request, 'weather/index.html', {'weather_data': weather_data})
    else:
        return JsonResponse({'error': 'City not found'}, status=404)

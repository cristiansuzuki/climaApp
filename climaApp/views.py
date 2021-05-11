from django.shortcuts import render
import urllib.request
import json
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=chicago&units=metric&appid=9f71ebf55a524813aad471af8983a1e3&lang=pt_br').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "feels_like": str(list_of_data['main']['feels_like'])+ ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
            "name": str(list_of_data['name']),
        }
        print(data)
    else:
        data = {}
        
        
    return render(request, "index.html", data)



#Pagina de erro 500
def page_error(request):
    return render(request, "500.html")

#Pagina de erro 400
def page_error(request):
    return render(request, "400.html")
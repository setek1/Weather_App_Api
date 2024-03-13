import datetime
import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    #Ingresar api key de sitio https://openweathermap.org/
    API_KEY=''
    #URL clima Actual
    current_weather_url="https://api.openweathermap.org/data/2.5/weather?q={}&lang=sp&appid={}"
   
    
    #Se obtiene el valor de la ciudad en el caso contrario se redirigira a una pagina de error.
    if request.method =="POST":
        city= request.POST['city']
        #Enviamos la informacion 
        weather_data =fetch_weather_forecast(city, API_KEY,current_weather_url)
    else:
        return render(request, 'index.html')
    
    context={
        'weather_data':weather_data,
        
    }

    return render(request,'index.html', context)

def fetch_weather_forecast(city, api_key, current_weather_url):
    #Solicitud  desde la api en formato json
    response= requests.get(current_weather_url.format(city,api_key)).json()
    #Obtenemos latitud y longitud a traves de la respuesta que nos de el response anterior.
    
    
    
    #Guardamos solo la informacion que necesitamos para poder visualizarla en formato de diccionario
    weather_data={
        'city':city,
        'hora':datetime.datetime.fromtimestamp(response['dt']).strftime('%H:%M'),
        'temperature':round(response['main']['temp']- 273.15,2),
        'description':response['weather'][0]['description'],
        'icon':response['weather'][0]['icon'],
        'country':response['sys']['country']
    }
    
    print(weather_data)


    return weather_data






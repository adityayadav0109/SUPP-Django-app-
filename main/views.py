from asyncio.windows_events import NULL
from django.shortcuts import render
import requests
from main.models import Feedback
API_KEY_NEWS = 'cb32ea1e9876436a9fc1d339b3aac1fe'
API_KEY_WEATHER ='1c486a426240dd14435695a1d434c7b5'
# Create your views here.

def home(request):
    return render(request, "main/index.html")

def savefeedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")

    savefdbk = Feedback(name = name, email = email, description = desc)
    savefdbk.save()
    return render(request, "main/index.html", {"msg": "ThankYou for your valuable Feedback"})
    
def about(request):
    return render(request, "main/about.html")


def about_dev(request):
    return render(request, "main/about_dev.html")

def news(request):
    url = f'https://newsapi.org/v2/everything?q=Apple&from=2022-02-28&sortBy=popularity&apiKey={API_KEY_NEWS}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {'articles' : articles}
    return render(request, "main/news.html", context)

def weather(request):
    city_name = NULL
    if(request.method == "POST"):
        city_name = request.POST['city']


        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY_WEATHER}'
        response = requests.get(url)
        data = response.json()
        context = {
            'city' : city_name,
            'temp' : round(data['main']['temp'] - 273),
            'desc' : data['weather'][0]['description'],
            'icon' : data['weather'][0]['icon'],
        }
        
        wthr = {'context' : context}
        return render(request, "main/weather.html", wthr)
    else:
        return render(request, "main/weather.html")

    

def search(request):
    return render(request, "main/search.html")
from django.shortcuts import render
import requests

def home(request):
    response = requests.get("https://omdbapi.com/?apikey=38b4b85b&s=Harry-Potter&type=movie")
    response_json = response.json()
    movies = response_json["Search"]
    context = {
        "movies": movies
    }
    return render(request, "index.html", context)
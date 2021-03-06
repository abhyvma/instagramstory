from django.shortcuts import render
import requests
import json

def instagramstory(request):
    
    con={'mytext':"Hello World"}
    return render(request, 'instagramstory.html', con)

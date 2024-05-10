from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .utils import *

# Create your views here.

reverse = reverseMapLang() # reverse is a dictionary with format {'language_name': 'language_code'}

def home(request):
    options = dropOptions() # options is a dictionary with format {'language_code': 'language_name'}
    
    context={
        "name":"Rahul",
        "option":options.values(),
        "reverse":reverse
    }
    return render(request, "index.html", context)

def get_new_value(request):
    text = request.GET.get('text', '')
    src = request.GET.get('src', 'auto')
    dest = request.GET.get('dest')
    dest = reverse[dest]
    # call your Python function here
    new_value = your_python_function(text,src,dest)
    return JsonResponse({'new_value': new_value})

def translate_speech(request):
    dest = request.GET.get('dest')
    src = request.GET.get('src')
    src = reverse[src]
    print("Source is",src)
    text = Speech_recognize(src)
    # dest = reverse[dest]
    translated_text = your_python_function(text,src,dest)

    return JsonResponse({
        'translated_text': translated_text,
        'Spoken_text': text
    })

def get_voice(request):
    text = request.GET.get('text')
    src = request.GET.get('src')
    src = reverse[src]
    audio_path = text_to_speech(text, src)
    
    return JsonResponse({'audio_path': audio_path})
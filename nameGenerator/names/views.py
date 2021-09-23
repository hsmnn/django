from django.shortcuts import render
from wonderwords import RandomWord

def index(request):
    return render(request, 'names/index.html')

def generate(request):
    r = RandomWord()
    adj = r.word(include_parts_of_speech=["adjectives"])
    name = r.word(include_parts_of_speech=["nouns"])
    fullName = adj + "_" + name
    context = {'name': fullName}
    return render(request, 'names/index.html', context)
from django.shortcuts import redirect, render
from django.views.generic.base import View
from wonderwords import RandomWord
from .models import Name

class IndexView(View):
    def index(request):
        latestName = Name.objects.last()
        return render(request, 'names/index.html', {'name': latestName})

    def generate(request):
        r = RandomWord()
        adj = r.word(include_parts_of_speech=["adjectives"])
        name = r.word(include_parts_of_speech=["nouns"])
        fullName = adj + " " + name
        n = Name()
        n.name = fullName
        n.save()
        return redirect('/')
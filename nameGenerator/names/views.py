from django.shortcuts import render
from django.views.generic.base import View
from wonderwords import RandomWord

class IndexView(View):
    def index(self, request):
        return render(request, 'names/index.html')

    def generate(sefl, request):
        r = RandomWord()
        adj = r.word(include_parts_of_speech=["adjectives"])
        name = r.word(include_parts_of_speech=["nouns"])
        fullName = adj + "_" + name
        context = {'name': fullName}
        return render(request, 'names/index.html', context)
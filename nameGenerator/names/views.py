from django.shortcuts import redirect, render
from django.views.generic.base import View
from wonderwords import RandomWord

class IndexView(View):
    def index(request):
        context = {}
        if (request.session.get('name') != ""):
            context['name'] = request.session.get('name')
        return render(request, 'names/index.html', context)

    def generate(request):
        r = RandomWord()
        adj = r.word(include_parts_of_speech=["adjectives"])
        name = r.word(include_parts_of_speech=["nouns"])
        fullName = adj + " " + name
        request.session['name'] = fullName
        return redirect('/')
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .forms import AnimalForm
from .models import Animal

from .serializers import AnimalSerializer 
from rest_framework.response import Response
from rest_framework.decorators import api_view

class Animais(TemplateView):
    template_name = "animais/animais.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['animais'] = Animal.objects.all()
        return context

def add_animal(request, *args, **kwargs):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form = AnimalForm()
    ctx = {'form': form}
    return render(request, 'animais/animal.html', ctx)

@api_view(['GET'])
def animaisApi (request, *args, **kwargs):
    animais = Animal.objects.all()
    data = AnimalSerializer(animais, many=True).data
    return Response(data)
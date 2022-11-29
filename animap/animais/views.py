from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from .forms import AnimalForm
from .models import Animal
from .serializers import AnimalSerializer 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
class Animais(LoginRequiredMixin, TemplateView):
    template_name = "animais/animais.html"
    login_url = 'accounts/login/'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['animais'] = Animal.objects.all()
        return context

@login_required
def add_animal(request, *args, **kwargs):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('success.html')
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
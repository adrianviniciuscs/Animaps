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
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

class Animais(LoginRequiredMixin, TemplateView):
    template_name = "animais/animais.html"
    login_url = 'login'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['animais'] = Animal.objects.all()
        return context

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('login')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'signup.html', {'form_usuario': form_usuario})

@login_required(login_url='login')
def deslogar_usuario(request):
    logout(request)
    return render(request, 'logged_out.html')

@login_required(login_url='login')
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('add_animal')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('add_animal')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

@login_required(login_url='/login')
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
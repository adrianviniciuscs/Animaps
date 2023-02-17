from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from .forms import AnimalForm
from .models import Animal
from .serializers import AnimalSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .pdfgenerator import gerarPDF
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType




class Animais(PermissionRequiredMixin,LoginRequiredMixin, TemplateView):
    permission_required = ('can_delete_animal_entry', 'can_change_entry')
    template_name = "animais/lista-animais.html"
    login_url = 'login'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['animais'] = Animal.objects.all()
        return context


class DashboardAnimal(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = ('can_delete_animal_entry', 'can_change_entry')
    model = Animal
    template_name = 'animais/dashboard-animal.html'


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('login')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'signup.html', {'form_usuario': form_usuario})

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

@login_required(login_url='login')
def deslogar_usuario(request):
    logout(request)
    return render(request, 'logged_out.html')


@login_required(login_url='login')
def dashboardUser(request):
    useranimais = Animal.objects.filter(user=request.user)
    return render(request, 'animais/dashboard-user.html', {'useranimais': useranimais})

@permission_required(['can_delete_animal_entry', 'can_change_entry'])
def gerarRelatorio(request):
    entry_id = request.GET.get('entry_id')

    pdf_data = gerarPDF(entry_id)

    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content Disposition'] = 'attachment; filename="report.pdf"'
    return response

@permission_required(['can_delete_animal_entry', 'can_change_entry'])
def update_estado_view(request):
    if request.method == 'POST':
        entry_id = request.POST.get('entry_id')
        estado = request.POST.get('state')

        entry = Animal.objects.get(id=entry_id)
        entry.state = state
        entry.save()

        return HttpResponseRedirect(reverse('dashboardAnimal', args=[entry_id]))
    else:
        return redirect('dashboardAnimal')

@permission_required(['can_delete_animal_entry', 'can_change_entry'])
def deletar_animal_view(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('animais')

    
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

@login_required(login_url='/login')
def add_animal(request, *args, **kwargs):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            
        else:
            print(form.errors)
    form = AnimalForm()
    ctx = {'form': form}
    return render(request, 'animais/add-animal.html', ctx)


@api_view(['GET'])
def animaisApi(request, *args, **kwargs):
    animais = Animal.objects.all()
    data = AnimalSerializer(animais, many=True).data
    return Response(data)

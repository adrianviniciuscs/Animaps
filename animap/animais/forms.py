from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
    )
    endereço = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
    )
    descriçao = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
    )
    ponto_ref = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
    )
    coordX = forms.CharField(
        widget=forms.HiddenInput()
    )
    coordY = forms.CharField(
        widget=forms.HiddenInput()
    )
    foto = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
    )

    class Meta:
        model = Animal
        fields = ['username', 'endereço', 'descriçao', 'ponto_ref', 'coordX', 'coordY', 'foto']

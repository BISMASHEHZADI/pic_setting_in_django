from django import forms 
from .models import Movie_Model
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
class Movie_Form(forms.ModelForm):
    class Meta:
        model = Movie_Model
        fields = ['movie_name','discription','image','owner']
        widgets = {

            'movie_name': forms.TextInput(attrs={'class':'form-control'}),
            'discription': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'owner': forms.Select(attrs={'class':'form-control'}),
        }


class Register(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        


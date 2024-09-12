from django.contrib.auth import logout
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from .forms import Movie_Form,Register
from .models import Movie_Model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.
def movie_add(request):
    if request.method == 'POST':
        form = Movie_Form(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('/')
    else:
        form = Movie_Form()
    return render(request, 'add_movie.html', {'form': form})

@login_required
def show_movie(request):
    movies = Movie_Model.objects.all()
    return render(request,'show_movie.html', {'movies': movies})
@login_required
def delete(request,id):
    movie = Movie_Model.objects.get(id=id)
    movie.delete()
    return HttpResponseRedirect('/show/')

@login_required
def edit(request,id):
    if request.method == 'POST':
        movie = Movie_Model.objects.get(id=id)
        form = Movie_Form(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            form = Movie_Form()
    else:
        movie = Movie_Model.objects.get(id=id)
        form = Movie_Form(instance=movie) 
                                    
    return render(request, 'edit.html', {'form': form})

@login_required
def detail(request,id):
    detail = Movie_Model.objects.get(id=id)
    return render(request, 'detail.html', {'detail': detail})


def register_view(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            form = Register()
        
    else:
        form = Register()
    return render(request,'registration/register.html',{'form':form})
            

# def logout_view(request):
#     if request.method == "POST":
#         logout(request)
#         return render(request,'logout.html')  # Redirect to home or any other page
#     else:
#         return redirect('/')  # If GET request, redirect user
            
            

def logoutv(request):
    logout(request)
    return HttpResponseRedirect('logout/')

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'AppCoder/home.html')

@login_required 
def post(request):

      if request.method == 'POST':

            myForm = PostForm(request.POST) #aquí mellega toda la información del html

            print(myForm)

            if myForm.is_valid:   #Si pasó la validación de Django

                  information = myForm.cleaned_data

                  post = Post (title=information['title'], subtitle=information['subtitle'], image=information['image'],
                  author=information['author'], text=information['text'],) 

                  post.save()

                  return render(request, "AppCoder/add_post.html") #Vuelvo al inicio o a donde quieran

      else: 

            myForm= PostForm() #Formulario vacio para construir el html

      return render(request, "AppCoder/add_post.html", {"myForm":myForm})

def inicio(request):
      bienvenido = "Bienvenido"
      return render(request, "AppCoder/inicio.html", {"Bienvenido":bienvenido})

class SearchResultsView(ListView):
    model = Post
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(subtitle__icontains=query) | Q(author__icontains=query) | Q(date__icontains=query) | Q(text__icontains=query)
        )
        return object_list

def search(request):
    if request.GET():
        pst=request.GET()
        post=Post.objects.filter(post=pst)
        if len(post)!=0:
            return render(request, "Appcoder/Searchresults.html", {"post":post})
        else:
            return render(request, "Appcoder/Searchresult.html", {"mesage": "There is no post"})
    else:
        return render(request, "Appcoder/searchPost.html", {"mensaje": "Didn't send data to search"})

#----- Login, logout y registro de usuarios

def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid():
            usu=request.POST["username"]
            psswrd=request.POST["password"]

            user=authenticate(username=usu, password=psswrd)
            if user is not None:
                login(request, user)
                return render(request, 'AppCoder/inicio.html', {'mensaje':f"Welcome {user}"})
            else:
                return render(request, 'AppCoder/login.html', {"form":form, 'mesage':'Wrong Username or Password'})
        else:
            return render(request, 'AppCoder/login.html', {"form":form, 'mensaje':'Wrong Username or Password'})
    else:
        form=AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'form':form})


def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]

            form.save()
            return render(request, 'AppCoder/inicio.html', {'mensaje':f"User {username} created"})
    else:
        form=UserRegisterForm()
    return render(request, 'AppCoder/register.html', {'form':form})

        
@login_required        
def editProfile(request):
    user=request.user
    if request.method=="POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            user.first_name=form.cleaned_data["first_name"]
            user.last_name=form.cleaned_data["last_name"]
            user.email=form.cleaned_data["email"]
            user.password1=form.cleaned_data["password1"]
            user.password2=form.cleaned_data["password2"]
            user.save()
            return render(request, 'AppCoder/inicio.html', {'mensaje':f"{user} Profile Edited"})
    else:
        form= UserEditForm(instance=user)
    return render(request, 'AppCoder/edit_Profile.html', {'form':form, 'user':user})


def addAvatar(request):
    if request.method == 'POST':
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            oldAvatar=Avatar.objects.filter(user=request.user)
            if(len(oldAvatar)>0):
                oldAvatar.delete()
            avatar=Avatar(user=request.user, imagen=form.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppCoder/inicio.html', {'user':request.user, 'mesage':'AVATAR ADDED SUCCESFULLY', "image":getAvatar(request)})
    else:
        form=AvatarForm()
    return render(request, 'AppCoder/addAvatar.html', {'form':form, 'usuario':request.user, "imagen":getAvatar(request)})

def getAvatar(request):
    list=Avatar.objects.filter(user=request.user)
    if len(list)!=0:
        image=list[0].image.url
    else:
        image=""
    return image

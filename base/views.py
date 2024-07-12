from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    rooms  = Room.objects.all()
    context = {"rooms":rooms}
    return render(request, "base/home.html",context=context)

@login_required(login_url="home")
def room_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    rooms = Room.objects.filter(title__contains=q)
    context = {"rooms":rooms}
    return render(request, "base/rooms.html",context=context)

@login_required(login_url="home")
def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form  = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            return redirect('room_list')
    context = {"form":form}
    return render(request, "base/form.html",context=context)

# def logoutuser(request):
def loginPage(request):

    page = "login"
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist!")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request,"Password Incorrect")
    context={"page":page}
    return render(request, "base/login.html", context=context)

def registerPage(request):
    page = "register"
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error("An error has occured during registration")
    context = {"page":page, "form" : form}
    return render(request,"base/login.html",context=context)
def logoutUser(request):
    logout(request)
    return redirect("home")

@login_required(login_url="home")
def chatRoom(request,pk):
    room = Room.objects.get(id=pk)
    chat_messages = room.message_set.all()
    context={"room":room,"chat_messages":chat_messages}
    return render(request,"base/chat_room.html",context=context)
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "base/home.html")

def room_list(request):
    

    return render(request, "base/rooms.html")
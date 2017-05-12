from django.shortcuts import render
import re
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.shortcuts import render, redirect

# Create your views here.
def reg_view(request):
    if (request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']
        if re.match(r'^[A-Za-z\d]{6,}$', password):
            if User.objects.filter(username=email).exists():
                return render(request, "reg.html")
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()

                user = authenticate(username=email, password=password)
                login(request, user)
                return redirect("index")
        else:
            return render(request, "reg.html")
    else:
        return render(request, "reg.html")


def log_view(request):
    if (request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('index')
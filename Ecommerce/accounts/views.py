from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def login_page(request):
    return render(request,'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email =request.POST.get("email")
        password = request.POST.get("password")
        USER_OBJ = User.objects.filter(username = email)

        if USER_OBJ.exists():
            messages.error(request,'Email already exists')
            return HttpResponse(request.path_info)
    

        user_obj = User.objects.create(first_name=first_name,last_name=last_name,email=email,username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.warning(request,'Email has been sent on your registerd email address')
        return HttpResponse(request.path_info)
    return render(request,'register.html')

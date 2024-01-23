from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def crud(request):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)
    

  
def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

    user = Student.objects.create(name=name,email=email,age=age)
    user.save()

    user = Student.objects.all()
    context = {"data":user}
    print(name,email,age)   
    return redirect("/")  
 
def updateData(request,id):
    if request.method=="POST":

        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        # gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        # edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    data=Student.objects.get(id=id) 
    context={"data":data}
    return render(request,"update.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")
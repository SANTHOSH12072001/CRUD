from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import MyRegisterForm
from .models import RegisterForm


# Create your views here.
def home(request):
    datas=RegisterForm.objects.all()
    if datas != "":
        return render(request,'home.html',{'datas':datas})
    else:
        return render(request,'home.html')

def insert(request):
    if request.method=="POST":
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Registered Successfully")
                return redirect("home")
            except:
                pass

    else:
        form = MyRegisterForm()
    return render(request,"registration.html",{'form':form})

def update(request,id):
    data=RegisterForm.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        address = request.POST['address']
        contact = request.POST['contact']

        data.name=name
        data.age = age
        data.email = email
        data.address = address
        data.contact = contact
        data.save()
        messages.success(request, "Updated Successfully")
        return redirect('home')
    return render(request,'update.html',{'data':data})

def delete(request,id):
    data = RegisterForm.objects.get(id=id)
    data.delete()
    messages.error(request, "Deleted Successfully")
    return redirect('home')
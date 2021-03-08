from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.db import IntegrityError
from .forms import UploadForm
from .models import Upload

# Create your views here.
def home(request):
    return render(request,'web/home.html')
def signupuser(request):
    if request.method=="GET":
        return render(request,'web/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('/')
            except IntegrityError:
                return render(request,'web/signupuser.html',{'form':UserCreationForm(),'error':'username has already taken'})
        else: 
            return render(request,'web/signupuser.html',{'form':UserCreationForm(),'error':'password didnot match'})


def loginuser(request):
    if request.method=="GET":
        return render(request,'web/loginuser.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user  is None:
            return render(request,'web/loginuser.html',{'form':AuthenticationForm(),'error':'username n password sidnot match'})

        else:
            login(request,user)
            return redirect('upload')
def logoutuser(request):
    if request.method=="POST":
        logout(request)
        return redirect('/')


def upload(request):
    if request.method=="POST":
        form = UploadForm(request.POST,request.FILES) 
        if form.is_valid():
            image = form.cleaned_data.get("image")
            obj=Upload.objects.create(image=image) 
            obj.save() 
            print(obj)
            return redirect('detailview')
        else:
            form=UploadForm()
            return render(request, "web/upload.html",{'form':form}) 
    else:
        return render(request,'web/upload.html',{'form':UploadForm()})

    return render(request,'web/upload.html',{'form':UploadForm()})
# def upload(request): 
#     context = {} 
#     if request.method == "POST": 
#         form = UploadForm(request.POST, request.FILES) 
#         if form.is_valid():
#             image = form.cleaned_data.get("image") 
#             obj = Upload.objects.create(  
#                                  image = image
#                                  ) 
#             obj.save() 
#             print(obj)
#             return redirect('/')
#     else: 
#         form = UploadForm() 
#         context['form']= form 
#     return render(request, "web/upload.html", context) 

# def upload(request):
#     if request.method=="GET":
#         return render(request,'web/upload.html',{'form':UploadForm()})
#     else:
#         form=UploadForm(request.POST)
#         if form.is_valid():
#             image=form.cleaned_data.get("image")
#             obj=Upload.objects.create(image=image)
#             obj.save()
#             return redirect('/')
        
#     return render(request,'web/upload.html',{'form':UploadForm()})
    
    

def detailview(request):
    image=Upload.objects.all()
    return render(request,'web/detailview.html',{'images':image})
    return render(request,'web/upload.html',{'images':image})

        
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'html/ltr/vertical-menu-template/login.html')

def register(request):
    return render(request,'html/ltr/vertical-menu-template/page-auth-register-v1.html')

def logout(request):
    return render(request,'html/ltr/vertical-menu-template/login.html')

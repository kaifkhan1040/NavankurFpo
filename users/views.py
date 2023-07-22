from django.views import generic
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ResetPasswordForm, fporegistration
from django.core.mail import send_mail
from .models import ForgetPassMailVerify, FpoEmailVerify
from .models import CustomUser
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import check_password
from app.models import FPO

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'html/ltr/vertical-menu-template/page-auth-register-v1.html'


# def login(request):
#     if request.method == 'POST':
#         email = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=email, password=password)
#         if email is not None:
#             form = login(request)
#             messages.success(request, f' welcome {email} !!')
#             return redirect('index')
#         else:
#             messages.info(request, f'account done not exit plz sign in')
#     form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form, 'title': 'log in'})


# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        # username = request.POST.get('username',None)
        email = request.POST.get('email', None)
        # print(email)
        password = request.POST.get('password', None)
        # print(password)
        remember_me = request.POST.get('remember_me', None)
        print('remember_me', remember_me)
        # if username is not None and password is not None:
        if email is not None and password is not None:
            # user = authenticate(request, username=username, password=password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if remember_me != None:
                    request.session.set_expiry(60 * 60 * 24 * 30 * 365)
                # response = HttpResponse()
                # response[email] = password
                # request.set_cookie(email, password, max_age = None, expires = None)
                # print('&' * 10)
                # print(response[email])
                response = HttpResponseRedirect(reverse_lazy('app:home'))
                if remember_me != None:
                    response.set_cookie('user', user)
                return response
                # return redirect('/')
            messages.error(request, 'Username and password is Invalid')
    return render(request, 'registration/login.html', {'user': request.user})


def reset_password(request):
    form = ResetPasswordForm()
    msg = 'Enter your email and we will send you instructions to reset your password'
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        email = request.POST.get('forgot-password-email')
        # email = request.POST.get('email')
        # print(print'the email is',email)
        if (CustomUser.objects.filter(email=email).exists()):
            email = CustomUser.objects.get(email=email)
            token = get_random_string(16)
            # print('token is',token)
            ForgetPassMailVerify(user_id=email.id, link=token).save()
            token = 'http://127.0.0.1:8000/user/reset_password/' + token
            # print('the whole url is ',token)

            email_send(token, email,email_message='Please verify your email for changing the password',email_subject='Reset Password')
            msg = 'The activation link has been send to your Email.'
        else:
            messages.error(request, 'email is not exists')
        # print('the email is', email)

    # return render(request,'user_basic.html')
    return render(request, 'registration/password_reset.html',
                  {'form': form, 'msg': msg})
    # return render(request, 'html/ltr/vertical-menu-template/page-auth-forgot-password-v1.html',
    #               {'form': form, 'msg': msg})


def email_send(token, email,email_message,email_subject):
    send_mail(
        email_subject,
        email_message +' '+ token,
        # 'radiantinfonet901@gmail.com',
        # 'mohdkaif@radiantinfonet.com',
        # 'admin@navankur.org',
        'support@navankur.org',
        [email],  #target email
        # fail_silently=False,
    )


def create_password(request, id):
    if (ForgetPassMailVerify.objects.filter(link=id).exists()):
        obj = ForgetPassMailVerify.objects.get(link=id)
        if obj.verify == False:
            if request.method == 'POST':
                password = request.POST.get('reset-password-new')
                con_pass = request.POST.get('reset-password-confirm')
                print(password,con_pass)
                # print(obj.user)
                if password == con_pass:
                    change_pass = CustomUser.objects.get(email=obj.user)
                    change_pass.set_password(password)
                    change_pass.save()
                    obj.verify = True
                    obj.save()
                    messages.success(request, 'Password change successfully!Please Login')
                    return redirect('user:login')
                else:
                    messages.error(request, 'Password not match')
            return render(request, 'registration/reset-password.html')
            # return render(request, 'html/ltr/vertical-menu-template/page-auth-reset-password-v1.html')
        messages.error(request, 'This link not valid')
    return redirect('user:reset_password')


def changepassword(request):
    print(request.method)
    if request.method == "POST":
        oldpass = CustomUser.objects.get(email=request.user)
        print('oldpass:', oldpass.password)
        password = request.POST.get('password')
        new_password = request.POST.get('new-password')
        confirm_password = request.POST.get('confirm-new-password')
        print('pass:', password, "new:", new_password, 'con:', confirm_password)
        if (new_password == confirm_password):
            print('enter pass')
            if (check_password(password, oldpass.password)):
                print('old pass')
                oldpass.set_password(new_password)
                oldpass.save()
                messages.success(request, 'Password change successfully')
            else:
                messages.error(request, 'Old password not found')
        return redirect('/admin/page_account')
    return redirect('/admin/page_account')


def Fporegistation(request):
    form = fporegistration()
    if request.method == 'POST':
        form = fporegistration(request.POST, request.FILES)
        if form.is_valid():
            email = request.POST.get('email')
            if (CustomUser.objects.filter(email=email).exists()):
                messages.error(request, 'Email already register')
            else:
                obj = form.save(commit=False)
                obj.role = 'admin'
                obj.is_active = False
                obj.save()
                # fpo.user_id=a.email
                # fpo.save()
                # obj2=FpoEmailVerify()
                # obj2.user=CustomUser.objects.get(email=email)
                # obj2.save()
                token = get_random_string(16)
                email = CustomUser.objects.get(email=email)

                # print('token is',token)
                FpoEmailVerify(user=email, link=token).save()
                token = 'http://127.0.0.1:8000/user/Fpoverify/' + token
                # print('the whole url is ',token)

                email_send(token, email,email_message='Please click given link to verify your email ',email_subject='Registration Verification')
                msg = 'The activation link has been send to your Email.'
                messages.success(request, 'Registration completed successfully Please check your registered email for verification')
                return redirect('user:Fporegistation')
        else:
            print(form.errors)
    return render(request, 'registration/register.html', {'form': form})
    # return render(request, 'html/ltr/vertical-menu-template/page-auth-register-v1.html', {'form': form})


# def Farmerregistation(request):
#     form = farmerregistration()
#     if request.method == 'POST':
#         form =farmerregistration(request.POST, request.FILES)
#         if form.is_valid():
#             email=request.POST.get('email')
#             if (CustomUser.objects.filter(email=email).exists()):
#                 messages.error(request, 'Email already register')
#             else:
#                 obj=form.save(commit=False)
#                 obj.role='admin'
#                 obj.save()
#                 messages.success(request, 'FPO added successfully')
#                 return redirect('app:Fpo')
#         else:
#             print(form.errors)
#     return render(request, 'html/ltr/vertical-menu-template/page-auth-register-v1.html', {'form': form})


def Fpoverify(request, id):
    if (FpoEmailVerify.objects.filter(link=id).exists()):
        obj = FpoEmailVerify.objects.get(link=id)
        obj.verify = True
        obj.save()
        obj1 = CustomUser.objects.get(email=obj.user.email)
        obj1.is_active = True
        messages.success(request, 'Email verified successfully Please login')
    return redirect('app:home')

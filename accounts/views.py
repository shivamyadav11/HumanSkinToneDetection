from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import html
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Profile
import random
# Create your views here.

# register route


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST['confirm_password']
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'User Already exist')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.info(request, 'Email Already exist')
                        return redirect('register')
                    else:
                        request.session['username'] = username
                        request.session['email'] = email
                        request.session['password'] = password
                        otp = []
                        num = str(random.randint(1000, 9999))
                        for x in num:
                            otp.append(x)
                        context = {'name': username, 'auth_otp': otp}
                        html_content = render_to_string(
                            'accounts/email.html', context)
                        text_content = strip_tags(html_content)

                        send_mail = EmailMultiAlternatives(
                            "Account email verification",
                            text_content,
                            settings.EMAIL_HOST_USER,
                            [email]
                        )
                        send_mail.attach_alternative(html_content, 'text/html')
                        send_mail.send()
                        # user_obj = User(username=username, email=email)
                        # user_obj.set_password(password)
                        # user_obj.save()
                        profile = Profile(
                            user=email, auth_otp=num)
                        profile.save()
                        return redirect('verify')
    return render(request, 'accounts/register.html')


# login route
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Invalid Username or Password")
                return redirect('login')
    return render(request, 'accounts/login.html')

# verify route


def verify(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            count = Profile.objects.filter(
                user=request.session['email']).count()
            profile = Profile.objects.filter(
                user=request.session['email'])
            if request.POST.get('auth_otp') == profile.values('auth_otp')[count-1]['auth_otp']:
                user = User.objects.create_user(
                    username=request.session['username'], password=request.session['password'], email=request.session['email'])
                user.save()
                auth.login(request, user)
                profile.delete()
                context = {'name': request.session['username']}
                html_content = render_to_string(
                    'accounts/confirm_email.html', context)
                text_content = strip_tags(html_content)

                send_mail = EmailMultiAlternatives(
                    "Registration Successfull",
                    text_content,
                    settings.EMAIL_HOST_USER,
                    [request.session['email']]
                )
                send_mail.attach_alternative(html_content, 'text/html')
                send_mail.send()
                return redirect('home')
            profile.delete()
            messages.info(request, "Invalid otp or email register again!")
            return redirect('register')
    return render(request, 'accounts/verify.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

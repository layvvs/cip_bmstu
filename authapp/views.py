from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from .forms import CreateUserForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@.*bmstu\.ru$'
    return re.match(pattern, email) is not None

def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            messages.success(request, 'Вы уже в системе.')
            return redirect('/')
        return render(request, 'authapp/login.html')
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user:
        login(request, user)
        messages.success(request, 'Вы успешно вошли.')
        return redirect('/')
    return render(request, "authapp/login.html", {"error": "Invalid login credentials"})

def logout_view(request: HttpRequest):
    logout(request)
    messages.success(request, 'Вы успешно вышли.')
    return redirect('/')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('/authapp/login')
    else:
        messages.error(request, "Activation link is invalid!")
    return redirect('/')

def activate_email(request, user, to_email):
    mail_subject = "Activate your user account."
    print('hi')
    message = render_to_string("authapp/activate_account.html", {
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    print(123)
    print(message)
    email = EmailMessage(mail_subject, message, to=[to_email])
    print(321)
    n = email.send()
    print('n: ', n)
    if n == 1:
        print('suc')
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        print('er')
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def signup_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            messages.success(request, 'Вы уже в системе.')
            return redirect('/') 
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if validate_email(email):             
                user = form.save(commit=False)
                user.is_active = False
                activate_email(request, user, email)
                user.save()
                return redirect('/')
            else:
                form.add_error('email', 'Используйте электронную почту с доменом bmstu')
    context = {'form': form}
    return render(request, 'authapp/signup.html', context)

from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.decorators.cache import cache_page
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from asgiref.sync import async_to_sync, sync_to_async

from user.forms import LoginForm, RegisterForm, ForgetPasswordForm, ResetPasswordForm

from user.models import PasswordResetUrl


# Create your views here.
async def login_form(request):
    """
        A Simple Login Form to authenticate users.
    """

    @sync_to_async()
    def auth_user(_username, _password):
        return authenticate(request, username=_username, password=_password)

    @sync_to_async()
    def login_user(_user):
        auth_login(request, user=_user)

    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = await auth_user(_username=username, _password=password)
            if user is not None:
                await login_user(_user=user)

                next_url = request.GET.get("next", None)

                if next_url:
                    return redirect(next_url)

                return redirect(reverse('home'))
            elif user is None:
                return render(request, 'accounts/login/unsuccessful/index.html')
    elif request.method == "GET":
        form = LoginForm()
    return render(request, 'accounts/login/index.html', {'form': form})


@cache_page(300)
@login_required()
@async_to_sync
async def logout(request):
    @sync_to_async()
    def authenticate_logout():
        auth_logout(request)

    if request.method == "GET":
        await authenticate_logout()
        return redirect(reverse('home'))
    else:
        raise Http404


@async_to_sync
async def register_form(request):
    """
        A Simple User Register Form
    """

    @sync_to_async
    def auth_user(_request, _username, _password):
        return authenticate(request=_request, username=_username,
                            password=_password)

    @sync_to_async
    def create_user(__username, __email, __first_name, __last_name, __password):
        User.objects.create(username=__username, email=__email, first_name=__first_name, last_name=__last_name,
                            password=__password).save()

    @sync_to_async
    def check_if_user(_username):
        return bool(User.objects.filter(username=username).exists())

    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_1 = form.cleaned_data['password_1']
            password_2 = form.cleaned_data['password_2']

            if (password_1 == password_2) and first_name and last_name and username and email:
                if await check_if_user(_username=username):
                    return render(request, 'accounts/register/user_exists/index.html')
                await create_user(__username=username, __email=email, __first_name=first_name,
                                  __last_name=last_name,
                                  __password=[password_1 if password_1 == password_2 else '12345678'][0])

                user = await auth_user(request, username, password_1)
                if user is not None:
                    auth_login(request, user)
                return redirect(reverse('register_success'))

            else:
                return redirect(reverse('register_form'))
    elif request.method == "GET":
        form = RegisterForm()
    return render(request, 'accounts/register/index.html', {'form': form})


@login_required()
@cache_page(300)
@async_to_sync
async def register_success(request):
    if request.method == 'GET':
        return render(request, 'accounts/register/success/index.html')
    else:
        raise Http404


@async_to_sync
async def forget_password_form(request):
    @sync_to_async
    def send_mail_function(email_subject, email_reset_message, from_sender, to_receiver):
        send_mail(
            email_subject,  # subject
            email_reset_message,  # message
            from_sender,  # from email
            [to_receiver]  # to email
        )

    @sync_to_async
    def check_if_user_exists(user_object):
        return User.objects.filter(username=user_object).exists()

    @sync_to_async
    def get_user(user_object):
        return User.objects.get(username=user_object)

    @sync_to_async
    def get_url(user_object):
        return PasswordResetUrl.objects.get(user=user_object).url

    @sync_to_async
    def password_reset_database(user_object):
        return PasswordResetUrl.objects.create(user=user_object)

    @sync_to_async
    def save_database(database):
        database.save()

    form = ForgetPasswordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            if await check_if_user_exists(username):
                user = await get_user(username)
                reset_object = await password_reset_database(user)

                password_reset_url = reset_object.url

                await save_database(reset_object)

                subject = 'Reset Password!'
                reset_message = f'''
                Hello, 
                This is an automated message. 
                You are getting this message because someone requested a password reset on your account.
                Click  https://127.0.0.1/accounts/reset/{password_reset_url}/ to reset your password.
                '''
                sender_email = settings.EMAIL_HOST_USER
                receiver_email = user.email
                await send_mail_function(
                    email_subject=subject,
                    email_reset_message=reset_message,
                    from_sender=sender_email,
                    to_receiver=receiver_email,
                )

                return render(request, 'accounts/forget/successful/index.html')
            elif not await check_if_user_exists(username):
                return render(request, 'accounts/forget/unsuccessful/index.html')
            else:
                raise Http404
    elif request.method == "GET":
        form = ForgetPasswordForm()
    return render(request, 'accounts/forget/index.html', {'form': form})


@async_to_sync
async def reset_password_form(request, url: str):
    @sync_to_async()
    def check_if_url_exists():
        return PasswordResetUrl.objects.filter(url=url).exists()

    @sync_to_async()
    def reset_password_from_user_model(_password):
        username = PasswordResetUrl.objects.filter(url=url).last().user

        user_object = User.objects.get(username__exact=username)
        user_object.set_password(_password)
        user_object.save()
        PasswordResetUrl.objects.get(url=url).delete()

    form = ResetPasswordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            password_1 = form.cleaned_data['password_1']
            password_2 = form.cleaned_data['password_2']
            if password_1 == password_2:
                await reset_password_from_user_model(_password=[password_1 if password_1 == password_2 else None][0])

                return render(request, 'accounts/reset/successful/index.html')
            return render(request, 'accounts/reset/unsuccessful/index.html')
    elif request.method == 'GET':
        if await check_if_url_exists():
            form = ResetPasswordForm()
        else:
            raise Http404
    return render(request, 'accounts/reset/index.html', {'form': form})

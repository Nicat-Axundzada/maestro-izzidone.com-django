from django.shortcuts import render, redirect, get_object_or_404
from account.forms import SignUpForm, LoginForm, CustomSetPasswordForm
from django.contrib.auth import login, logout, authenticate
# Custom forget password
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from account.models import PasswordResetToken
from django.utils import timezone
from account.forms import CustomPasswordResetForm
from account.models import CustomUser

# Create your views here.


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Services:index')
    else:
        form = SignUpForm()

    return render(request, 'account/signup.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Services:index')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('Services:index')


def password_reset(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(email=email).first()

            if user:
                token = get_random_string(length=32)

                reset_token = PasswordResetToken(user=user, token=token)
                reset_token.save()

                reset_url = f"{request.scheme}://{request.get_host()}/account/reset/{token}/"

                subject = 'Password Reset'
                message = f'Click the following link to reset your password: {reset_url}'
                from_email = settings.EMAIL_HOST_USER
                to_email = [email,]

                send_mail(subject, message, from_email,
                          to_email, fail_silently=False)

                messages.success(
                    request, 'Password reset email sent. Check your inbox.')
                return redirect('account:password_reset_done')

    else:
        form = CustomPasswordResetForm()

    return render(request, 'account/reset_password.html', {'form': form})


def password_reset_done(request):
    return render(request, 'account/reset_password_sent.html')


def password_reset_confirm(request, token):
    reset_token = get_object_or_404(PasswordResetToken, token=token)

    if (timezone.now() - reset_token.created_at).total_seconds() > 24 * 60 * 60:
        messages.error(request, 'Password reset link has expired.')
        return redirect('account:password_reset')

    if request.method == 'POST':
        form = CustomSetPasswordForm(reset_token.user, request.POST)
        if form.is_valid():
            form.save()
            reset_token.delete()
            messages.success(request, 'Password reset successfully.')
            return redirect('account:password_reset_complete')
    else:
        form = CustomSetPasswordForm(reset_token.user)

    return render(request, 'account/reset.html', {'form': form})


def password_reset_complete(request):
    return render(request, 'account/reset_password_complete.html')

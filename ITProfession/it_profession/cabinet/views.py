from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


@login_required
def cabinet_view(request):
    responses = request.user.forms.all().order_by('-created_at')
    return render(request, 'cabinet/cabinet.html', {'responses': responses})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно! Войдите в аккаунт.")
            return redirect('cabinet')
    else:
        form = UserCreationForm()
    return render(request, 'cabinet/register.html', {'form': form})

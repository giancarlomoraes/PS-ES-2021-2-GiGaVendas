from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


@login_required
def index(request):
    return render(request, 'core/index.html')


# Tela de alteração de Senha do Usuário por parte do próprio Usuário
@login_required
def self_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'core/user/self-change-password.html', {'form': form})

import uuid

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.forms import SignUpForm
from core.tasks import add_invitation_bonus

from core.models import User, InvitationCode


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            add_invitation_bonus(form.cleaned_data.get('promo_code'))
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def create_invitation_code(request):
    invitation_code = InvitationCode.objects.create(user=request.user, invitation_code=str(uuid.uuid1()))

    return render(request, 'invitation_code.html', {'invitation_code': invitation_code})
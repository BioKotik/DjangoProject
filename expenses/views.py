from django.shortcuts import render, get_object_or_404, redirect
from expenses.models import Record, Profile
from expenses.forms import SendEmailForm, LoginForm
from django.core.mail import send_mail
from django.views.generic import ListView

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

# Create your views here.
def all_records(request):
    records = Record.objects.all().order_by('date')
    return render(request, 'workplace.html', {'records': records})

class RecordListView(ListView):
    queryset = Record.objects.all()
    context_object_name = 'records'
    template_name = 'workplace.html'

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authentificated successfully')
                else:
                    return HttpResponse('Disabled user')
            else:
                return HttpResponse('Invalid credentials (login or password)')
    else:
        form = LoginForm()
    return render(request, 'log-in.html', {'form': form})
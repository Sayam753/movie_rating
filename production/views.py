from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from production import forms
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import ProfileOfActor, ProfileOfDirector, ProfileOfProduction, ProfileOfUser
gr = {
    'a':'is_production_company',
    'b':'is_actor',
    'c':'is_director',
    'd':'public_user'
}

def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=gr[request.POST['group']])
            user.groups.add(group)
            if(str(group)=='is_actor'):
                p=ProfileOfActor.objects.create(user=user)
            elif(str(group)=='is_director'):
                p=ProfileOfDirector.objects.create(user=user)
            elif(str(group)=='is_production_company'):
                p=ProfileOfProduction.objects.create(user=user)
            else:
                p=ProfileOfUser.objects.create(user=user)
            p.save()
            messages.success(request,f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = forms.UserRegisterForm()
    return render(request,'production/register.html',{'form':form})

@login_required
def profile_for_production(request):
    return render(request,'production/profile_production.html')


@login_required
def profile_for_actor(request):
    return render(request,'production/profile_actor.html')

@login_required
def profile_for_user(request):
    return render(request,'production/profile_user.html')

@login_required
def profile_for_director(request):
    return render(request,'production/profile_director.html')

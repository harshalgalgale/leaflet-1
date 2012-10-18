from django.contrib.auth.models import User
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from accounts.forms import RegistrationForm, LoginForm
from django.core.urlresolvers import reverse
from django.contrib import messages

# Messages
INFO = 20
SUCCESS = 25
ERROR = 40

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'leaves', 'votes']

def registration_request(request):
    if request.user.is_authenticated():
        return redirect(reverse('profile'))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], 
                                            email=form.cleaned_data['email'], 
                                            password=form.cleaned_data['password'])
            user.save()
            return redirect(reverse('index'))
        else:
            return render(request, 'register.html', {
                'form':form
            })
    else:
        # User is not submitting form, show them blank registration
        form = RegistrationForm()
        return render(request, 'register.html', {
            'form':form
        })

def login_request(request):
    if request.user.is_authenticated():
        return reverse(index)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('create'))
            else:
                # Invalid User or Pass
                messages.add_message(request, ERROR, 'You have provided invalid login information.')
                return render(request, 'login.html', {
                    'form':form
                })
        else:
            # Blank
            messages.add_message(request, ERROR, 'Please enter correct login information.')
            return render(request, 'login.html', {
                'form':form
            })
    else:
        # No POST, Show Form
        messages.add_message(request, INFO, 'Please login below.')
        return render(request, 'login.html', {
            'form':LoginForm(),
        })

def logout_request(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def profile_detail(request):
    return render(request, 'profile.html')

@login_required
def profile_update(request):

    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            messages.add_message(request, SUCCESS, 'Your profile has been updated successfully.')
        else:
            messages.add_message(request, ERROR, 'Something went wrong.')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile_update.html', {
        'userprofile': form,
    })

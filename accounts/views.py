from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from accounts.forms import RegistrationForm, LoginForm
from django.core.urlresolvers import reverse

def registration_request(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], 
                                            email=form.cleaned_data['email'], 
                                            password=form.cleaned_data['password'])
			user.save()
			return HttpResponseRedirect('/')
		else:
			return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
	else:
	    # User is not submitting form, show them blank registration
	    form = RegistrationForm()
	    return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

def login_request(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render_to_response('login.html', {'form':form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form':form}, context_instance=RequestContext(request))
    else:
        # user is not submitting form, show login form
        form = LoginForm()
        return render_to_response('login.html', {'form':form}, context_instance=RequestContext(request))

def logout_request(request):
	logout(request)
	return redirect(reverse('index'))

def profile(request, user_id):
	return render_to_response('profile.html', context_instance=RequestContext(request))

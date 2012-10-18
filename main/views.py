from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html')

@login_required
def create(request):
	return render(request, 'create.html')

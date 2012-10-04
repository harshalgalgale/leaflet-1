from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

@login_required
def create(request, user_id):
	return render_to_response('create.html', context_instance=RequestContext(request))

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import Http404
from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView
from understand.models import Result
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from understand.forms import TextSummary, Register
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.cache import cache_control, never_cache
from django.urls import reverse
from django.contrib import auth
from django.views.generic import TemplateView, ListView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.sessions.backends.base import SessionBase
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.middleware.csrf import rotate_token
from django.utils.crypto import constant_time_compare
from django.utils.module_loading import import_string
from django.http import JsonResponse
from django.db.models import DEFERRED
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseServerError
from understand.filters import ResultFilter

users = User.objects.values_list('username')

user = []

for i in range(len(users)):
    user.append(users[i][0])

def error404(request, exception, template_name="understand/404.html"):
    response = render(request, 'understand/404.html', {})
    response.status_code = 404
    return response

def error500(request, template_name="understand/500.html"):
    response = render(request, 'understand/500.html', {})
    response.status_code = 500
    return response

def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'created an account for {username}')
            return redirect('Login')
    else:
        form = Register()

    return render(request, 'understand/register.html', context={'form': form})

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('SSubmit')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'understand/login.html', {})

@method_decorator(login_required, name='dispatch')
def logout(request, *args, **kwargs):
    auth.logout(request)
    for key in request.session.keys():
        del request.session[key]
    return redirect('Login')

board_de = [login_required, never_cache]
@method_decorator(board_de, name='dispatch')
class Submit(LoginRequiredMixin,TemplateView):
	template_name = "understand/submit.html"

	def get(self, request):
		form = TextSummary()
		return render(request, self.template_name, {'form':form})

	def post(self,request):
		form = TextSummary(request.POST)
		title = ''
		source = ''
		original_text = ''
		summarized_text = ''
		category = ''
		user = ''
		if form.is_valid():
			title = form.cleaned_data['title']
			source = form.cleaned_data['source']
			original_text = form.cleaned_data['original_text']
			summarized_text = form.cleaned_data['summarized_text']
			category = form.cleaned_data['category']
			user = form.cleaned_data['user']
			form.save()
			return redirect('SSubmit')
		args = {
		'title': title,
        'form':form,'source':source,
        'original_text':original_text,
        'summarized_text':summarized_text,
		'category':category,'user':user}
		return render(request, self.template_name, args)

board_de = [login_required, never_cache]
@method_decorator(board_de, name='dispatch')
class Data(LoginRequiredMixin,TemplateView):
	login_url = 'Login'
	redirect_field_name = 'DataS'

	def get(self,request):
		result = Result.objects.all().order_by('-date')
		result_filter = ResultFilter(request.GET, queryset=result)
		search = result_filter.qs
		args = {
		 'result': result,
		 'filter': result_filter,
		 'search': search
		}
		return render(request, 'understand/data.html',args)

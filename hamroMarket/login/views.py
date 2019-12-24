from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from login.forms import SignupForm
from django.contrib.auth import login as auth_login, authenticate

# Create your views here.
def login(request):
    return HttpResponse("<h2> welcome to login</h2>")

def template_loader(request):
    template = loader.get_template('index_product.html')
    return HttpResponse(template.render())

@csrf_protect
def signup(request):
    if request.method == 'POST':
        signup = SignupForm(request.POST)
        if signup.is_valid():
            user = signup.save()
            user.set_password(user.password)
            user.save()
            username = user.username
            # password = user.password garda encrypted password auxa
            raw_password = signup.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('/show')

    if request.method == 'GET':
        csrfContext = RequestContext(request)
        signup_form = SignupForm()
        return render(request, 'register.html', {'signup_form': signup_form}, csrfContext)







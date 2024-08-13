from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('accounts:user_login')
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print('Success')
            return redirect('accounts:profile') 
        else:
            print('Invalid username or password')
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'accounts/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('accounts:login')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def about_view(request):
    return render(request, 'pages/about.html')

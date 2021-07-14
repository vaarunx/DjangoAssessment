from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserForm , ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request , f'Account Created For {username}! Please login')
            return redirect('login')
            
    else:
        u_form = UserForm()
    return render(request, 'blog/register.html' , {'u_form' : u_form})


@login_required
def dashboard(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , instance=request.user)
        p_form = ProfileUpdateForm(request.POST , instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f'Your account has been updated!')
            return redirect('dashboard')

    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    return render(request , 'blog/dashboard.html' , {'u_form': u_form , 'p_form': p_form} )    


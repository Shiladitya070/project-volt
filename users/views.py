from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterFrom, UserUpdatedForm,ProfileUpdateFrom
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == "POST":
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Your account has been created {username}!Now you can login')
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request,'users/register.html',{'form': form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdatedForm(request.POST,instance=request.user)
        p_form = ProfileUpdateFrom(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdatedForm(instance=request.user)
        p_form = ProfileUpdateFrom(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html', context)
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterFrom, UserUpdatedForm
from django.contrib.auth.decorators import login_required


# def register(request):
#     if request.method == "POST":
#         form = UserRegisterFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             messages.success(
#                 request, f'Your account has been created {username}!Now you can login')
#             return redirect('login')
#     else:
#         form = UserRegisterFrom()
#     return render(request, 'users/register.html', {'form': form})

def register(request):


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdatedForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdatedForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)

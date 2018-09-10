from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # This will do all the update in the database
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {}'.format(username))
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

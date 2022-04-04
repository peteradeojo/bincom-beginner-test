from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(r):
    if r.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=r.POST)
        if form.is_valid():
            user = form.save()
            login(r, user)
            return redirect('tasks:index')

    context = {'form': form}
    return render(r, 'registration/register.html', context)

# views.py
from django.shortcuts import render, redirect

from myapp.models import ContactMessage
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def user_list(request):
    # Retrieve all users
    users = ContactMessage.objects.all().values()

    return render(request, 'user_list.html', {'users': users})



def details(request ,id):
    # Retrieve all users
    users = ContactMessage.objects.get(id=id)

    return render(request, 'details.html', {'user': users})
from django.shortcuts import render, redirect
from .forms import User
import phonenumbers
from phonenumbers import PhoneNumberFormat
from phonenumbers.phonenumberutil import NumberParseException
from django.shortcuts import render, redirect
from .forms import UserProfileForm

def user_form(request):
    if request.method == 'POST':
        # If the form was submitted, process the data
        form = User(request.POST)
        if form.is_valid():
            # Form data is valid, save the user profile
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        # If it's a GET request, display the empty form
        form = User()

    return render(request, 'user_form.html', {'form': form})

def success(request):
    # You can create a success page template or handle it as needed
    return render(request, 'success.html')


from django.shortcuts import render, redirect
from .forms import User

def User(request):
    if request.method == 'POST':
        # If the form was submitted, process the data
        form = User(request.POST)
        if form.is_valid():
            # Form data is valid, save the user profile
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        # If it's a GET request, display the form with any previous user input
        form = User()

    return render(request, 'user_form.html', {'form': form})

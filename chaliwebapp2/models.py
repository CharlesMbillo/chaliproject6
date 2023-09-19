from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class User(models.Model):
    # Define the first name field with a maximum length of 30 characters
    first_name = models.CharField(max_length=30)

    # Define the last name field with a maximum length of 30 characters
    last_name = models.CharField(max_length=30)

    # Define the phone number field with a regex validator for a valid phone number format
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phonenumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Optional field

    # Define the email field with an email validator
    email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address.")])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

        def user_form(request):
            if request.method == 'POST':
            # If the form was submitted, process the data
                form = UserForm(request.POST)
            if form.is_valid():
                # Validate the phone number using phonenumbers library
                phonenumber = form.cleaned_data['phone_number']
            try:
                parsed_number = phonenumbers.parse(phonenumber, None)
                if not phonenumbers.is_valid_number(parsed_number):
                    form.add_error('phonenumber', 'Invalid phone number format')
                else:
                    form.save()
                    return redirect('profile_success')  # Redirect to a success page
            except NumberParseException:
                form.add_error('phone_number', 'Invalid phonenumber format')
            else:
        # If it's a GET request, display the empty form
                    form = UserForm()

        return render(request, 'user_profile.html', {'form': form})


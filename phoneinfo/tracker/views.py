# tracker/views.py
from django.shortcuts import render
from .forms import PhoneNumberForm
import phonenumbers
from phonenumbers import carrier, geocoder

def phone_info(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            parsed_number = phonenumbers.parse(phone_number)
            country = geocoder.description_for_number(parsed_number, "en")
            service_provider = carrier.name_for_number(parsed_number, "en")
            return render(request, 'tracker/phone_info.html', {
                'form': form,
                'country': country,
                'service_provider': service_provider
            })
    else:
        form = PhoneNumberForm()
    return render(request, 'tracker/phone_info.html', {'form': form})

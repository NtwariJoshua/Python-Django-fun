from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import SubscriberForm
from .forms import AddressForm
from .models import Subscriber


def subscribe_new(request, template='subscribers/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        address = AddressForm(request.POST)
        if form.is_valid() and address.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
            user.set_password(password1)
            user.save()

            # Save the Address
            address_one = address.cleaned_data['address_one']
            address_two = address.cleaned_data['address_two']
            city = address.cleaned_data['city']
            state = address.cleaned_data['state']

            sub = Subscriber(address_one=address_one, address_two=address_two,
                             city=city, state=state, user_rec=user)
            sub.save()
            auth = authenticate(username=username,password=password1)

            if auth is not None:
                if auth.is_active:
                    login(request, auth)
                    # TODO: Redirect User To Dashboard
                    return HttpResponseRedirect('/sign-up')
                else:
                    # TODO: Redirect User to Proper Login Page
                    return HttpResponseRedirect('django.contrib.auth.views.login')
            else:
                return HttpResponseRedirect('/sign-up')
        else:
            return HttpResponse(form.errors.as_json())
    else:
        form = SubscriberForm
        address = AddressForm
        return render(request, template, {'form': form, 'address': address})

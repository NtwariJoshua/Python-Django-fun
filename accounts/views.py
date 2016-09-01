from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Account
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import NewAccountForm
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404


class AccountList(ListView):
    model = Account
    paginate_by = 12
    template_name = 'account/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):

        try:
            a = self.request.GET.get('account', )
        except KeyError:
            a = None
        if a:
            account_list = Account.objects.filter(name__icontains=a, owner=self.request.user)
        else:
            account_list = Account.objects.filter(owner=self.request.user)

        return account_list

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)


@login_required()
def account_details(request, uuid):
    account = Account.objects.get(uuid=uuid)
    if account.owner != request.user:
        return HttpResponseForbidden()
    variables = {
        'account': account
    }

    return render(request, 'accounts/account_details.html', variables)


@login_required()
def create_new_account(request, uuid=None):
    account = None
    if uuid:
        account = get_object_or_404(Account, uuid=uuid)
        if account.owner != request.user:
            return HttpResponseForbidden
        else:
            account = Account(owner=request.user)
    if request.method == 'POST':
        form = NewAccountForm(request.POST, instance=account)
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            phone = form.cleaned_data['phone']

            account = Account(
                name=name,
                desc=desc,
                address_one=address_one,
                address_two=address_two,
                city=city,
                state=state,
                phone=phone,
                owner=request.user)
            account.save()
            return HttpResponseRedirect(reverse('account-list'))
    else:
        form = NewAccountForm(instance=account)
        variables = {
            'form': form,
            'account': account
        }
        if request.is_ajax():
            template = 'accounts/account_item_form.html'
        else:
            template = 'accounts/new-account.html'
        return render(request, template, variables)

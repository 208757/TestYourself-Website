from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"],
                                password=cd["password"])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    response = "Uwierzytelnienie zakończyło się sukcesem."
                    return HttpResponse(response)
                else:
                    return HttpResponse("Konto jest zablokowane.")
            else:
                return HttpResponse("Nieprawidłowe dane uwierzytelniające.")
    else:
        form = LoginForm()
        return render(request, 'authentication/login.html')


def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            if cd['password'] == cd['password2']:
                new_user.set_password(cd['password'])
                new_user.save()
                return render(request, "authentication/register_done.html", {
                    'new_user': new_user
                    })
            else:
                return HttpResponse("Nie utworzono konta")
        else:
                print(form.errors)
                return HttpResponse("Nie prawidłowy formularz")

    else:
        form = RegistrationForm()
        print(form.as_p())
        return render(request, 'authentication/registration.html', {
            'user_form': form})

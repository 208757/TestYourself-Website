from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm


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
                    'new_user': new_user})
            else:
                return render(request, "authentication/error_message.html", {
                    "errors": {"password2": ["Podałeś różne hasła"]}})
        else:
                print(form.errors)
                print(type(form.errors))
                for x in form.errors.items():
                    print(x)
                return render(request, "authentication/error_message.html", {
                    "errors": form.errors})
    else:
        parameters = [("id_username", "username", "Nazwa użytkownika", "glyphicon glyphicon-user", "text"),
            ("id_first_name", "first_name", "Imię", "glyphicon glyphicon-user", "text"),
            ("id_last_name", "last_name", "Nazwisko", "glyphicon glyphicon-user", "text"),
            ("id_email", "email", "Adres e-mail", "glyphicon glyphicon-envelope", "text"),
            ("id_password", "password", "Hasło", "glyphicon glyphicon-lock", "password"),
            ("id_password2", "password2", "Powtórz hasło", "glyphicon glyphicon-lock", "password")
        ]

        return render(request, 'authentication/registration.html', {
            'parameters': parameters
        })

def validate(request, username, email_address):
    parameters = {"username": True, "email": True}
    if username == ".":
        parameters["username"] = False
    if email_address == ".":
        parameters["email"] = False
    for user in User.objects.all():
        if username != "." and user.get_username() == username:
            parameters["username"] = False
        if user.email == email_address:
            parameters["email"] = False
    return JsonResponse(parameters)

def startpage(request):
    return render(request, 'app/event.html')
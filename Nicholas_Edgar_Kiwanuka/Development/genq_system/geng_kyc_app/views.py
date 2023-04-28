from django.shortcuts import render, redirect
from .forms import KYCRegistrationForm
from .models import KYC


def kyc_registration(request):
    if request.method == "POST":
        form = KYCRegistrationForm(request.POST)
        if form.is_valid():
            # save the data to the database
            kyc_registration = form.save()
            return redirect("success")
    else:
        form = KYCRegistrationForm()
    return render(request, "kyc_registration.html", {"form": form})


def success(request):
    return render(request, "success.html")

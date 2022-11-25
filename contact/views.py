from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["seanmeade.dev@gmail.com"])
            except BadHeaderError:
                messages.error(request, "Your message wasn't sent please try again.")
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contact/contact.html", {"form": form})


def success_view(request):
    form = ContactForm()
    messages.success(request, 'Thank you, your message has been sent.')
    return render(request, "contact/contact.html", {"form": form})

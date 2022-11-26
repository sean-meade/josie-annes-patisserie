from django.template.loader import render_to_string
from josie_annes_patisserie import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data["email"]
            name = form.cleaned_data["name"]
            subject = f"New message from {name}"
            content = form.cleaned_data['content']

            html = render_to_string('contact/email/contactform.html', {
                'name': name,
                'from_email': from_email,
                'content': content
            })
            try:
                send_mail(subject, content, from_email, ['seanpatmeade@gmail.com'], html_message=html)
                messages.success(request, "Your message has been sent")
            except Exception as e:
                messages.error(request, f"Could not send email - {e}")
            return redirect('contact')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from afternoon_tea.forms import AfternoonTeaForm
from afternoon_tea.models import AfternoonTea


def afternoon_tea(request):
    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'date': request.POST['date'],
            'time': request.POST['time'],
            'notes': request.POST['notes'],
            'under_review': True,
            'no_of_people': request.POST['no_of_people'],
        }
        afternoon_tea_form = AfternoonTeaForm(form_data)
        try:
            if afternoon_tea_form.is_valid():
                booking = afternoon_tea_form.save(commit=False)
                booking.save()

            return redirect(
                reverse(
                    'afternoon_tea_success',
                    args=[
                        booking.booking_number]))
        except Exception as e:
            messages.error(
                request, f"Please make sure number of people doesn't exceed 6")

    else:
        afternoon_tea_form = AfternoonTeaForm()

    template = 'afternoon_tea/afternoon_tea.html'
    context = {
        'afternoon_tea_form': afternoon_tea_form,
    }

    return render(request, template, context)


def afternoon_tea_success(request, booking_number):
    booking = get_object_or_404(AfternoonTea, booking_number=booking_number)

    messages.success(request, f'Booking successfully processed! \
            A confirmation email will be sent to {booking.email}.')

    template = 'afternoon_tea/afternoon_tea_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)

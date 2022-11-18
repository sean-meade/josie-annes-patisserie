from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from cake_order.forms import CakeForm
from cake_order.models import Cake

from datetime import datetime


def cake(request):
    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'date': datetime.strptime(request.POST.get('date'), "%d/%m/%Y").date(),
            'notes': request.POST['notes'],
            'under_review': True,
        }
        cake_form = CakeForm(form_data)
        print(request.POST.get('date'))
        try:
            if cake_form.is_valid():
                cake_order = cake_form.save(commit=False)
                cake_order.save()

                return redirect(reverse('cake_order_success', args=[cake_order.cake_order_number]))
        except Exception as e:
            messages.error(request, f'Error creating order: {e}')
            return HttpResponse(status=500)

    else:
        cake_form = CakeForm()

    template = 'cake_order/cake_order.html'
    context = {
        'cake_form': cake_form,
    }

    return render(request, template, context)


def cake_success(request, cake_order_number):
    cake_order = get_object_or_404(Cake, cake_order_number=cake_order_number)

    messages.success(request, f'Booking successfully processed! \
            A confirmation email will be sent to {cake_order.email}.')

    template = 'cake_order/cake_order_success.html'
    context = {
        'cake_order': cake_order,
    }

    return render(request, template, context)
